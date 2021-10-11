import scrapy


class ZhongshanSpider(scrapy.Spider):
    name = 'Zhongshan'
    allowed_domains = ['http://www.zs.gov.cn/']
    start_urls = ['http://http://www.zs.gov.cn//']

    def parse(self, response):
        pass
