import scrapy


class XiningSpider(scrapy.Spider):
    name = 'Xining'
    allowed_domains = ['http://www.xining.gov.cn/']
    start_urls = ['http://http://www.xining.gov.cn//']

    def parse(self, response):
        pass
