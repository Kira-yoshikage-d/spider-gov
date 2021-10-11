import scrapy


class ChaoyangSpider(scrapy.Spider):
    name = 'Chaoyang'
    allowed_domains = ['http://www.chaoyang.gov.cn/']
    start_urls = ['http://http://www.chaoyang.gov.cn//']

    def parse(self, response):
        pass
