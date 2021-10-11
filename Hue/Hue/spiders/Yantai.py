import scrapy


class YantaiSpider(scrapy.Spider):
    name = 'Yantai'
    allowed_domains = ['http://www.yantai.gov.cn/']
    start_urls = ['http://http://www.yantai.gov.cn//']

    def parse(self, response):
        pass
