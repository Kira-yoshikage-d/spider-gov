import scrapy


class LiuzhouSpider(scrapy.Spider):
    name = 'Liuzhou'
    allowed_domains = ['http://www.liuzhou.gov.cn/']
    start_urls = ['http://http://www.liuzhou.gov.cn//']

    def parse(self, response):
        pass
