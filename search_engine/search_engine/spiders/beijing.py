import scrapy


class BeijingSpider(scrapy.Spider):
    name = 'beijing'
    allowed_domains = ['www.beijing.gov.cn']
    start_urls = ['http://www.beijing.gov.cn/']

    api = 'http://www.beijing.gov.cn/so/ss/s'
    post_data_template = {
        'siteCode': '12',
        'tab': 'all',
        'timestamp': 'as',
        'wordToken': 'token',
        'page': '1',
        'pageSize': '20',
        'qt': '关键字',
        'timeOption': 0,
        'sort': 'relevance',
        'keyPlace': '0',
        'fileType': '',
    }
    header_fetch_token = {

    }



    def parse(self, response):
        pass
