import scrapy


class JinanDbSpider(scrapy.Spider):
    name = 'Jinan_db'
    allowed_domains = ['http://jnrb.e23.cn/']
    start_urls = ['http://http://jnrb.e23.cn//']

    def parse(self, response):
        pass
