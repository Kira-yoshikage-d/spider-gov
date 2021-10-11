import scrapy


class YuxiSpider(scrapy.Spider):
    name = 'Yuxi'
    allowed_domains = ['http://www.yuxi.gov.cn/']
    start_urls = ['http://http://www.yuxi.gov.cn//']

    def parse(self, response):
        pass
