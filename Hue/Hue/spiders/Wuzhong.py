import scrapy


class WuzhongSpider(scrapy.Spider):
    name = 'Wuzhong'
    allowed_domains = ['http://www.wuzhong.gov.cn/']
    start_urls = ['http://http://www.wuzhong.gov.cn//']

    def parse(self, response):
        pass
