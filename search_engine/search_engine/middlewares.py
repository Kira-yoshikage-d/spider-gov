# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from time import sleep
from typing import Optional, Tuple, Union, List
import requests
from scrapy.settings import json
import termcolor
from logging import exception
from requests import JSONDecodeError, request
from scrapy.shell import inspect_response
from scrapy import FormRequest, Request, Selector, Spider, signals
from search_engine import g_keywords
import copy
from collections import defaultdict, namedtuple
Token = namedtuple('Token', ["timestamp", "wordtoken", "suid", "cookies"])

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http.response import Response


class search_engineSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class search_engineDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        pass

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        spider.logger.debug(json.dumps(response.__dict__, indent=4))
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('debug: %s' % spider.name)

class PubProperty:
    token_url: str = "http://www.beijing.gov.cn/so/s?tab=all&siteCode=1100000088&qt={keyword}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    def __init__(self, keyword: str) -> None:
        self._keyword = keyword
        self.reinit(keyword=keyword)

    def _init(self, *args) -> None:
        _attrs = ['siteCode', 'tab', 'qt', 'debug', 'page', 'pageSize', 'timestamp', 
                  'wordToken', 'tabToken', 'tagParam', 'apiUrl', 'auto', 'multiSelect', 'suid']
        for key, val in zip(_attrs, args):
            setattr(self, key, val)

    def __repr__(self) -> str:
        return 'PubProperty Object with suid: ' + str(getattr(self, 'suid'))

    @staticmethod
    def parse_args(response: requests.Response) -> List[str]:
        selector = Selector(text=response.text)
        args_list: List[str] = [s.strip().replace("'", "").replace(",", "").split(".")[0] 
                                for s in selector.css("script::text").re(r'initPubProperty\(([\s\S]*?)\);')[0].strip().split('\r\n')]
        return args_list

    def reinit(self, keyword: Optional[str]=None):
        if not keyword:
            keyword = self._keyword
        response = requests.get(self.token_url.format(keyword=keyword), headers=self.headers)
        args_list = self.parse_args(response=response)
        self._init(*args_list)
        return self

    @property
    def query_info(self) -> Tuple[dict[str, str], dict[str, str]]:
        fields = ['siteCode', 'tab', 'timestamp', 'wordToken', 'page', 'pageSize', 'qt']
        data = { field: str(getattr(self, field)) for field in fields }
        data['pageSize'] = '20'
        data['sort'] = 'relevance'
        data['timeOption'] = '0'
        data['keyPlace'] = '0'
        data['fileType'] = ''
        headers: dict[str, str] = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
            'suid': getattr(self, 'suid'),
        }
        return data, headers

class WordTokenDownloaderMiddleware:
    token_cache: dict[str, PubProperty] = {}

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
        
    def spider_opened(self, spider):
        spider.logger.info(termcolor.colored('Spider opened: %s' % spider.name, 'red'))
        for keyword in g_keywords:
            sleep(1)
            self.token_cache[keyword] = PubProperty(keyword=keyword)

    def process_request(self, request: FormRequest, spider: Spider):
        # 1. 提取关键词，formdata
        # 2. 构造新的formdata
        # 3. 抛出新的请求
        if 'processed' in request.meta:
            return None
        keyword = request.meta['keyword']
        page = request.meta['page']
        pub_property = self.token_cache[keyword]
        formdata, headers = pub_property.query_info
        formdata['page'] = str(page)
        s = request.replace(
            formdata=formdata,
            meta={'keyword': keyword, 'formdata': formdata, 'page': page, 'processed': True},
            headers=headers,
            dont_filter=True
        )
        spider.logger.info(str(s))
        return s

    def process_response(self, request: Request, response: Response, spider: Spider):
        # 1. 检查请求是否成功
        # 2. 成功则直接返回原响应
        # 3. 不成功则删除token，获取新token，再返回请求
        try:
            data = response.json()
        except JSONDecodeError:
            ok = False
        except AttributeError:
            ok = False
        else:
            ok = data['ok']

        if ok:
            return response
        else:
            keyword: str = request.meta['keyword']
            page: str = request.meta['page']
            reason: str = data.get("msg", "unknown")

            spider.logger.debug(termcolor.colored(f"{keyword}: {page} not ok, refetching token...", "yellow"))
            spider.logger.debug(termcolor.colored(f"reason: {reason}", "yellow"))

            pub_property = self.token_cache[keyword].reinit()

            spider.logger.debug(termcolor.colored(f"{keyword}: {page} refetching done!".format(page=page, keyword=keyword), "yellow"))

            formdata, headers = pub_property.query_info
            formdata['page'] = str(page)
            s = request.replace(
                formdata=formdata,
                meta={'keyword': keyword, 'formdata': formdata, 'page': page, 'processed': True},
                headers=headers
            )
            return s

