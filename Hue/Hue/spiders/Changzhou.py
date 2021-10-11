import scrapy


class ChangzhouSpider(scrapy.Spider):
    name = 'Changzhou'
    allowed_domains = ['http://www.changzhou.gov.cn/']
    start_urls = ['http://http://www.changzhou.gov.cn//']

    def parse(self, response):
        pass
