from Hue.basepro import ZhengFuBaseSpider


class DalianDbSpider(ZhengFuBaseSpider):
    name = 'Dalian_db'
    allowed_domains = ['http://szb.dlxww.com/dlrb/']
    start_urls = ['http://http://szb.dlxww.com/dlrb//']



    def parse(self, response):
        pass
