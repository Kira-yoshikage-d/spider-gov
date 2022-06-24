import abc
import copy

import scrapy
from scrapy import FormRequest, Request
from scrapy.responsetypes import Response
from termcolor import colored

from Hue import g_keywords


class ZhengFuBaseSpider(scrapy.Spider):
    name = ''
    allowed_domains = ['']
    start_urls = ['']
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
    # 数据模板
    data = {}
    # 是否解析第一页
    parse_first = True
    # 起始页的索引 (某些情况下需要调整为 0 )
    start_page = 1

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

        self.logger.debug("check method")
        method = self.method
        if not method:
            raise Exception("Need method!")

        if method == "GET":
            yield from self.start_get_requests(page=self.start_page,
                                               callback=self.parse_index)
        elif method == "POST":
            yield from self.start_post_requests(page=self.start_page,
                                                callback=self.parse_index)
        else:
            raise Exception("Invalid method!")

    def start_get_requests(self, page=None, callback=None, meta=None):
        keywords = self.keywords
        api = self.api
        headers = self.headers
        for keyword in keywords:
            url = api.format(keyword=keyword, page=page)
            req = Request(url=url,
                          meta={"keyword": keyword},
                          headers=headers,
                          callback=callback)
            yield req

    def start_post_requests(self, page=None, callback=None):
        keywords = self.keywords
        url = self.api
        headers = self.headers
        self.logger.debug("爬取 第{}页".format(page))
        for keyword in keywords:
            data = self.build_data(keyword, page)
            req = FormRequest(url=url,
                              meta={"keyword": keyword},
                              headers=headers,
                              formdata=data,
                              callback=callback)
            yield req

    def parse_index(self, response: Response):
        parse_first = self.parse_first
        start_page = self.start_page
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
                yield from self.start_get_requests(page=page,
                                                   callback=self.parse_items)
        elif self.method == "POST":
            for page in range(start_page, end_page):
                yield from self.start_post_requests(page=page,
                                                    callback=self.parse_items)

    def build_data(self, keyword, page):
        data = copy.copy(self.data)
        data = self.edit_data(data, keyword, page)
        return data

    def parse_items(self, response):
        items_box = self.edit_items_box(response)
        items = self.edit_items(items_box)
        keyword = response.meta["keyword"]
        for item in items:
            yield self.parse_item(item, keyword)

    def parse_item(self, item, keyword):
        item = self.edit_item(item)
        item["keyword"] = keyword
        if not item["url"]:
            return None
        return item

    @abc.abstractmethod
    def edit_data(self, data: dict, keyword: str, page: int):
        """
        当请求方法为POST时应该发出的数据包
        input:
        data:dict
        return:
        data:dict
        """
        raise Exception("Must rewrite edit_data")

    @abc.abstractmethod
    def edit_items_box(self, response: Response):
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        raise Exception("Must rewrite edit_items_box")

    @abc.abstractmethod
    def edit_items(self, items_box):
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    @abc.abstractmethod
    def edit_item(self, item):
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
        raise Exception("Must rewrite edit_page")
