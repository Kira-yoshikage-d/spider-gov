import scrapy


class HuaibeiSpider(scrapy.Spider):
    name = 'Huaibei'
    allowed_domains = ['http://www.huaibei.gov.cn/']
    start_urls = ['http://http://www.huaibei.gov.cn//']

    def parse(self, response):
        pass
