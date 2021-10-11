import scrapy


class SanmingSpider(scrapy.Spider):
    name = 'Sanming'
    allowed_domains = ['http://www.sm.gov.cn/']
    start_urls = ['http://http://www.sm.gov.cn//']

    def parse(self, response):
        pass
