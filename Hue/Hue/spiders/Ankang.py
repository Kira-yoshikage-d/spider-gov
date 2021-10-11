import scrapy


class AnkangSpider(scrapy.Spider):
    name = 'Ankang'
    allowed_domains = ['http://www.ankang.gov.cn/']
    start_urls = ['http://http://www.ankang.gov.cn//']

    def parse(self, response):
        pass
