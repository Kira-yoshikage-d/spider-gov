import scrapy


class ChengduDbSpider(scrapy.Spider):
    name = 'Chengdu_db'
    allowed_domains = ['http://www.cdrb.com.cn/paperindex.htm']
    start_urls = ['http://http://www.cdrb.com.cn/paperindex.htm/']

    def parse(self, response):
        pass
