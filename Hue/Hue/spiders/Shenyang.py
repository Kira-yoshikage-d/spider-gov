import scrapy


class ShenyangSpider(scrapy.Spider):
    """GET"""
    name = 'Shenyang'
    allowed_domains = ['shenyang.gov.cn']
    start_urls = ['http://http://www.shenyang.gov.cn//']

    def parse(self, response):
        pass
