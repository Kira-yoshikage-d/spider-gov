import scrapy


class JianSpider(scrapy.Spider):
    name = 'Jian'
    allowed_domains = ['http://www.jian.gov.cn/']
    start_urls = ['http://http://www.jian.gov.cn//']

    def parse(self, response):
        pass
