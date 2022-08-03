import scrapy


class WeifangDbSpider(scrapy.Spider):
    name = 'Weifang_db'
    allowed_domains = ['http://wfrb.wfnews.com.cn/content']
    start_urls = ['http://http://wfrb.wfnews.com.cn/content/']

    def parse(self, response):
        pass
