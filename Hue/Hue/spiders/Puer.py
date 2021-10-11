import scrapy


class PuerSpider(scrapy.Spider):
    name = 'Puer'
    allowed_domains = ['http://www.puershi.gov.cn/']
    start_urls = ['http://http://www.puershi.gov.cn//']

    def parse(self, response):
        pass
