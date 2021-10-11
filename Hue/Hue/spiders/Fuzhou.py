import scrapy


class FuzhouSpider(scrapy.Spider):
    name = 'Fuzhou'
    allowed_domains = ['http://www.jxfz.gov.cn/']
    start_urls = ['http://http://www.jxfz.gov.cn//']

    def parse(self, response):
        pass
