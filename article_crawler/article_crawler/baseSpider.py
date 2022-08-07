from scrapy import Spider, Request
from scrapy.responsetypes import Response
from collections import defaultdict
from urllib.parse import urlparse
import os
import csv
from termcolor import colored


class baseSpider(Spider):
    """article_crawler 的基础爬虫"""
    parser_hooks = defaultdict(list)

    def __init__(self):
        super().__init__()
        self.file_path = os.path.join('data', 'uniq', 'uniq_' + self.name + '.csv')
        self.file_handler = open(self.file_path, 'rt')
        self.not_handled = []
        # TODO
        self.handled = []

    def start_requests(self):
        field_names = ['url', 'keyword']
        reader = csv.DictReader(self.file_handler, fieldnames=field_names)
        for item in reader:
            url = item['url']
            keyword = item['keyword']
            yield Request(url=url, meta={'url': url, 'keyword': keyword}, callback=self.main_parser)

    def main_parser(self, response: Response):
        url = response.meta['url']
        keyword = response.meta['keyword']
        for parser_func in self.parser_hooks[self.name]:
            try:
                result = parser_func(self, response)
                result = self.post_process(result, url=url, keyword=keyword)
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
        self.not_handled.append({'url': url, 'keyword': keyword})
        return None

    def result_pass(self, result):
        if all([col in result.keys() for col in ['content', 'title', 'date']]):
            return all([result[col] for col in ['content', 'title', 'date']])
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

    @staticmethod
    def close(spider, reason):
        spider.file_handler.close()
        spider.not_handled = sorted(spider.not_handled, key=lambda x: x['url'])
        spider.save_notHandled()
        spider.process_handled()

    def save_notHandled(self):
        with open(self.file_path, mode="wt") as csv_file:
            field_name = ['url', 'keyword']
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
            # csv_writer.writeheader()
            for item in self.not_handled:
                csv_writer.writerow(item)

    def process_handled(self):
        # 默认只分析主域名
        handled = [{'domain': urlparse(item['url']), 'parser': item['parser'].__name__}
                   for item in self.handled]
        # 去重
        handled = list(set(handled))
        # 排序
        handled = sorted(handled, key=lambda x: x['url'])
        summary = defaultdict(list)
        for item in handled:
            summary[item['parser']].append(item['domain'])
        pass
        # TODO

