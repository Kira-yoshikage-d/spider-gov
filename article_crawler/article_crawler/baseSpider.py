from scrapy import Spider, Request, settings
from scrapy.responsetypes import Response
from collections import defaultdict
from urllib.parse import urlparse
import os
import csv
from termcolor import colored
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings
from article_crawler.extensions.start_requests import RequestGenerator


class baseSpider(Spider):
    """article_crawler 的基础爬虫"""
    parser_hooks = defaultdict(list)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    def __init__(self):
        super().__init__()
        self.not_handled = []
        # TODO
        self.handled = []

    def start_requests(self):
        rg = RequestGenerator(self.name)
        for item in rg.fetch_url():
            request = Request(url=item['url'], headers=self.headers, callback=self.main_parser, meta={'url': item['url']})
            yield request

    def main_parser(self, response: Response):
        url = response.meta['url']
        for parser_func in self.parser_hooks[self.name]:
            try:
                result = parser_func(self, response)
                result = self.post_process(result, url=url)
            except Exception as e:
                self.logger.debug(colored("解析函数 {} : 出错: {}".format(parser_func.__name__, str(e)), "red"))
                result = None

            if result is not None and self.result_pass(result):
                self.handled.append({'url': url, 'parser': str(parser_func)})
                self.logger.debug(colored("解析成功.", "green"))
                return result
            else:
                self.logger.debug(colored("解析函数 {} : 解析失败: {}".format(parser_func.__name__, result), "yellow"))

        self.logger.debug(colored("没有对应的解析函数.", "red"))
        return None

    def result_pass(self, result):
        if all([col in result.keys() for col in ['content']]):
            return all([result[col] for col in ['content']])
        return False

    def post_process(self, result, **kwargs):
        for key, val in result.items():
            if isinstance(val, list):
                val = '\n'.join([v for v in val if v.strip()])
            if val:
                result[key] = val.strip()
        for key, val in kwargs.items():
            result[key] = val
        return result

    @classmethod
    def parser(cls, spider_name, url_example):
        def decorator(parser_func):
            cls.parser_hooks[spider_name].append(parser_func)
            parser_func.__str__ = lambda self: url_example
            return parser_func
        return decorator

