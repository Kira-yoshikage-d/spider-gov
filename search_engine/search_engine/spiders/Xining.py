import scrapy


class XiningSpider(scrapy.Spider):
    """试运行, 跳过"""
    name = '西宁'
    api = 'http://www.xining.gov.cn/'
    allowed_domains = ['http://www.xining.gov.cn/']
    start_urls = ['http://http://www.xining.gov.cn//']

    def parse(self, response):
        pass
