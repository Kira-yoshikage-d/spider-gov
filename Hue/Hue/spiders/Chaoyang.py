import scrapy


class ChaoyangSpider(scrapy.Spider):
    name = 'Chaoyang'
    allowed_domains = ['chaoyang.gov.cn']
    start_urls = ['http://chaoyang.gov.cn/']

    def parse(self, response):
        pass
