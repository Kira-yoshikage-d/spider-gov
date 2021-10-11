import scrapy


class SanyaSpider(scrapy.Spider):
    name = 'Sanya'
    allowed_domains = ['http://www.sanya.gov.cn/']
    start_urls = ['http://http://www.sanya.gov.cn//']

    def parse(self, response):
        pass
