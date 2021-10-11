import scrapy


class WeifangSpider(scrapy.Spider):
    name = 'Weifang'
    allowed_domains = ['http://www.weifang.gov.cn/']
    start_urls = ['http://http://www.weifang.gov.cn//']

    def parse(self, response):
        pass
