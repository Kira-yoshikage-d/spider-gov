import scrapy


class YuxiDbSpider(scrapy.Spider):
    name = 'Yuxi_db'
    allowed_domains = ['http://www.yxdaily.com/']
    start_urls = ['http://http://www.yxdaily.com//']

    def parse(self, response):
        pass
