import scrapy


class ChenzhouSpider(scrapy.Spider):
    name = 'Chenzhou'
    allowed_domains = ['http://www.czs.gov.cn/']
    start_urls = ['http://http://www.czs.gov.cn//']

    def parse(self, response):
        pass
