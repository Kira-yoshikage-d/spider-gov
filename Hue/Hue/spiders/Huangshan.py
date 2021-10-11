import scrapy


class HuangshanSpider(scrapy.Spider):
    name = 'Huangshan'
    allowed_domains = ['http://www.huangshan.gov.cn/']
    start_urls = ['http://http://www.huangshan.gov.cn//']

    def parse(self, response):
        pass
