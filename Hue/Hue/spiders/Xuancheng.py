import scrapy


class XuanchengSpider(scrapy.Spider):
    name = 'Xuancheng'
    allowed_domains = ['http://www.xuancheng.gov.cn/']
    start_urls = ['http://http://www.xuancheng.gov.cn//']

    def parse(self, response):
        pass
