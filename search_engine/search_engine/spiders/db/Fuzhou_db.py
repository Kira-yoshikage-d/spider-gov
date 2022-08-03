import scrapy


class FuzhouDbSpider(scrapy.Spider):
    name = 'Fuzhou_db'
    allowed_domains = ['http://ipaper.zgfznews.com/']
    start_urls = ['http://http://ipaper.zgfznews.com//']

    def parse(self, response):
        pass
