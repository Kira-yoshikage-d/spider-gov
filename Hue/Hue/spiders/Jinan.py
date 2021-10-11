import scrapy


class JinanSpider(scrapy.Spider):
    name = 'Jinan'
    allowed_domains = ['http://www.jinan.gov.cn/']
    start_urls = ['http://http://www.jinan.gov.cn//']

    def parse(self, response):
        pass
