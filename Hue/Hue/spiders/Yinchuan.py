import scrapy


class YinchuanSpider(scrapy.Spider):
    name = 'Yinchuan'
    allowed_domains = ['http://www.yinchuan.gov.cn/']
    start_urls = ['http://http://www.yinchuan.gov.cn//']

    def parse(self, response):
        pass
