import scrapy


class DalianSpider(scrapy.Spider):
    name = 'Dalian'
    allowed_domains = ['dl.gov.cn']
    start_urls = ['http://https://www.dl.gov.cn//']
    api = "https://www.dl.gov.cn/dhc/searchJs/retrieval?question={}&pageNum={}"
    keywords = []

    def build_api_url(self, keyword, page):
        if not keyword or not page:
            raise Exception("Need keyword or page")
        return self.api.format(keyword, page)

    def parse(self, response):
        pass
