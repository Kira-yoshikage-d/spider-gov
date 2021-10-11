import scrapy


class XiangtanSpider(scrapy.Spider):
    name = 'Xiangtan'
    allowed_domains = ['http://www.xiangtan.gov.cn/']
    start_urls = ['http://http://www.xiangtan.gov.cn//']

    def parse(self, response):
        pass
