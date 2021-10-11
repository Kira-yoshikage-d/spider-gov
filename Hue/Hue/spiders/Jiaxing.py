import scrapy


class JiaxingSpider(scrapy.Spider):
    name = 'Jiaxing'
    allowed_domains = ['http://www.jiaxing.gov.cn/']
    start_urls = ['http://http://www.jiaxing.gov.cn//']

    def parse(self, response):
        pass
