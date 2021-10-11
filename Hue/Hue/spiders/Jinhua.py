import scrapy


class JinhuaSpider(scrapy.Spider):
    name = 'Jinhua'
    allowed_domains = ['http://www.jinhua.gov.cn/']
    start_urls = ['http://http://www.jinhua.gov.cn//']

    def parse(self, response):
        pass
