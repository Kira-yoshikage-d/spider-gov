import scrapy


class ZhuzhouSpider(scrapy.Spider):
    name = 'Zhuzhou'
    allowed_domains = ['http://www.zhuzhou.gov.cn/']
    start_urls = ['http://http://www.zhuzhou.gov.cn//']

    def parse(self, response):
        pass
