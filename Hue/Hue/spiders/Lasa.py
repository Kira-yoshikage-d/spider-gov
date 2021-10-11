import scrapy


class LasaSpider(scrapy.Spider):
    name = 'Lasa'
    allowed_domains = ['http://www.lasa.gov.cn/']
    start_urls = ['http://http://www.lasa.gov.cn//']

    def parse(self, response):
        pass
