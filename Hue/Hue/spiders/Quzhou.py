import scrapy


class QuzhouSpider(scrapy.Spider):
    name = 'Quzhou'
    allowed_domains = ['http://www.qz.gov.cn/']
    start_urls = ['http://http://www.qz.gov.cn//']

    def parse(self, response):
        pass
