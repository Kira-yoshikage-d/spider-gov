import scrapy


class XiningDbSpider(scrapy.Spider):
    name = 'Xining_db'
    allowed_domains = ['http://www.xnwbw.com/paperindex.htm']
    start_urls = ['http://http://www.xnwbw.com/paperindex.htm/']

    def parse(self, response):
        pass
