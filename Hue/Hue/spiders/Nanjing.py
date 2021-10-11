import scrapy
from scrapy import Request


class NanjingSpider(scrapy.Spider):
    """ Ajax """
    name = 'Nanjing'
    allowed_domains = ['nanjing.gov.cn']
    start_urls = ['http://http://www.nanjing.gov.cn//']
    api = "https://www.nanjing.gov.cn/igs/front/search.jhtml?code=c1c8a0a187b3404a9e7e1b048f90610c&pageSize=10&searchWord={}&searchWord2={}&siteId=10"
    keywords = ["煤炭"]

    def start_requests(self):
        keywords = self.keywords
        if not keywords:
            raise Exception("Need a keyword!")
        for keyword in keywords:
            url = self.build_url(keyword)
            request = Request(
                    url=url,
                    callback=self.parse_index
                    )
            yield request
        
    def build_url(self, keyword):
        api = self.api
        url = api.format(keyword, keyword)
        return url

    def parse_index(self, response):
        yield from self.parse_item(response)
        raw_data = response.json()
        total_page = raw_data['page']['totalPages']
        url = response.url + "&pageNumber={}"
        for page in range(2, total_page+1):
            yield Request(
                    url = url.format(page),
                    callback = self.parse_item
                    )

    def parse_item(self, response):
        raw_data = response.json()
        page = raw_data['page']
        for item in page['content']:
            yield item
        # return (item for item in page['content'])

