import scrapy


class ChengduSpider(scrapy.Spider):
    name = 'Chengdu'
    allowed_domains = ['http://www.chengdu.gov.cn/']
    start_urls = ['http://http://www.chengdu.gov.cn//']

    def parse(self, response):
        pass
