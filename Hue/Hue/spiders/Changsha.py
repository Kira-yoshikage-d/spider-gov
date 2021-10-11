import scrapy


class ChangshaSpider(scrapy.Spider):
    name = 'Changsha'
    allowed_domains = ['http://www.changsha.gov.cn/']
    start_urls = ['http://http://www.changsha.gov.cn//']

    def parse(self, response):
        pass
