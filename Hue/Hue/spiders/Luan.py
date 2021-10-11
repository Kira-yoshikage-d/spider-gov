import scrapy


class LuanSpider(scrapy.Spider):
    name = 'Luan'
    allowed_domains = ['http://www.luan.gov.cn/']
    start_urls = ['http://http://www.luan.gov.cn//']

    def parse(self, response):
        pass
