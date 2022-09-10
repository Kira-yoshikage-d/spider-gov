import abc
import copy
from typing import Any, Iterable, Union
import logging

import scrapy
from scrapy import FormRequest, Request, Selector
from scrapy.shell import inspect_response
from scrapy.responsetypes import Response
from termcolor import colored

from search_engine import g_keywords

logging.getLogger('parso.cache').disabled=True
logging.getLogger('parso.cache.pickle').disabled=True


class ZhengFuBaseSpider(scrapy.Spider):
    name = ''
    start_urls = ['']
    allowed_domains = ['']
    # 关键字
    keywords = g_keywords
    # API
    api = ""
    # 模式 GET/POST
    method = "default"
    # 测试用 headers
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    cookie = ""
    # 数据模板
    data: dict[str, Any] = {}
    # 是否解析第一页
    parse_first = True
    # 起始页的索引 (某些情况下需要调整为 0 )
    start_page = 1
    # 启用关键词批量搜索
    batch = False
    # debug
    debug = False

    def start_requests(self):
        """
        抛出初始请求
        """
        self.logger.debug("check keywords")
        keywords = self.keywords
        if not keywords:
            raise Exception("Need keywords!")

        self.logger.debug("check API")
        api = self.api
        if not api:
            raise Exception("Need API!")
        if self.cookie:
            self.headers['cookie'] = self.cookie

        self.logger.debug("check method")
        method = self.method
        if not method:
            raise Exception("Need method!")

        if self.batch:
            self.logger.debug("enable batch mode")

        if method == "GET":
            yield from self.start_get_requests(page=self.start_page,
                                               callback=self.parse_index)
        elif method == "POST":
            yield from self.start_post_requests(page=self.start_page,
                                                callback=self.parse_index)
        else:
            raise Exception("Invalid method!")

    def start_get_requests(self, page=None, callback=None, meta=None, **kwargs):
        """抛出 GET 方法对应的起始请求."""
        keywords = self.keywords
        api = self.api
        headers = self.headers
        if self.batch:
            # GET 方法不提供批量搜索
            pass
        else:
            for keyword in keywords:
                url = api.format(keyword=keyword, page=page)
                req = Request(url=url,
                              meta={"keyword": keyword},
                              headers=headers,
                              callback=callback)
                yield req

    def start_post_requests(self, page=1, callback=None, **kwargs):
        """抛出 POST 方法对应的起始请求."""
        self.logger.debug("[func]: start_post_requests")
        keywords = self.keywords
        url = self.api
        headers = self.headers
        self.logger.debug("爬取 第{}页".format(page))
        if self.batch:
            keywords = g_keywords
            data = self.build_data(keywords, page, **kwargs)
            req = FormRequest(
                url=url,
                meta={"keyword": keywords},
                headers=headers,
                formdata=data,
                callback=callback
            )
            yield req
        else:
            for keyword in keywords:
                data = self.build_data(keyword, page, **kwargs)
                req = FormRequest(
                    url=url,
                    meta={"keyword": keyword},
                    headers=headers,
                    formdata=data,
                    callback=callback
                )
                yield req

    def parse_index(self, response: Response):
        """解析当前页，以及抛出余下请求."""
        parse_first = self.parse_first
        start_page = self.start_page

        ###########
        #  debug  #
        ###########
        if self.debug:
            inspect_response(response, self)

        # 获取总页数
        total_page = self.edit_page(response)
        self.logger.debug(
            colored(
                "关键字[{}] 总页数: {}".format(response.meta.get('keyword'),
                                         total_page), "red"))
        end_page = start_page + total_page
        if parse_first:
            start_page += 1
            # 解析当前页
            yield from self.parse_items(response)
        # 抛出余下页的请求
        if self.method == "GET":
            for page in range(start_page, end_page):
                yield from self.start_get_requests(
                    page=page,
                    callback=self.parse_items,
                    last_response=response,
                )

        elif self.method == "POST":
            for page in range(start_page, end_page):
                yield from self.start_post_requests(
                    page=page,
                    callback=self.parse_items,
                    last_response=response,
                )

    def build_data(self, keyword='煤炭', page=1, **kwargs):
        """从默认数据模板构造数据."""
        data = copy.copy(self.data)
        # 默认模板渲染
        data = self.render_data_template(data, keyword, page)
        # 开发接口
        data = self.edit_data(data, keyword, page, **kwargs)
        # 默认转换问字符串
        data = self.post_edit_data(data)
        return data

    def post_edit_data(self, data: dict[str, Any]) -> dict[str, str]:
        for key, val in data.items():
            data[key] = str(val)
        return data

    def render_data_template(self, data: dict[str, str], keyword: str, page: Union[int, str]) -> dict[str, str]:
        for key, val in data.items():
            if val == '{page}':
                data[key] = str(page)
            elif val == '{keyword}':
                data[key] = str(keyword)
            elif val == '{keywords}':
                data[key] = g_keywords
        return data


    def parse_items(self, response):
        items_box = self.edit_items_box(response)
        items = self.edit_items(items_box)
        keyword = response.meta["keyword"]
        if not items:
            return
        for item in items:
            yield self.parse_item(item, keyword)

    def parse_item(self, item, keyword):
        """解析item"""
        item = self.edit_item(item)
        item = self.post_parse_item(item, keyword)
        if not item["url"]:
            return None
        return item

    def post_parse_item(self, item, keyword) -> dict:
        """钩子函数，默认将关键字存入数据."""
        if not self.batch:
            item["keyword"] = keyword
        else:
            item['keyword'] = 'BATCH MODE'
            keywords = keyword
            for keyword in keywords:
                if keyword in item.get('title', '') or keyword in item.get('content', ''):
                    item['keyword'] = keyword
                    break
        return item

    ###############
    #  Interface  #
    ###############

    @abc.abstractmethod
    def edit_data(self, data: dict, keyword: str, page: int, **kwargs):
        """
        当请求方法为POST时应该发出的数据包
        input:
        data:dict
        return:
        data:dict
        kwagrs['last_response']
        """
        return data

    @abc.abstractmethod
    def edit_items_box(self, response: Response):
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def edit_items(self, items_box: Union[Selector, Iterable]):
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    @abc.abstractmethod
    def edit_item(self, item: Selector):
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        return item

    @abc.abstractmethod
    def edit_page(self, response: Response) -> int:
        """
        input: response
        return: int
        """
        raise NotImplementedError()

