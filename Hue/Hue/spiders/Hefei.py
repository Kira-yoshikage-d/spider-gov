import scrapy


class HefeiSpider(scrapy.Spider):
    name = 'Hefei'
    allowed_domains = ['http://www.hefei.gov.cn/']
    start_urls = ['http://http://www.hefei.gov.cn//']

    def parse(self, response):
        pass
