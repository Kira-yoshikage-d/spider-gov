import scrapy


class WuzhongDbSpider(scrapy.Spider):
    name = 'Wuzhong_db'
    allowed_domains = ['https://www.chinawznews.net/content/']
    start_urls = ['http://https://www.chinawznews.net/content//']

    def parse(self, response):
        pass
