import scrapy
from Hue.basepro import ZhengFuBaseSpider


class DalianSpider(ZhengFuBaseSpider):
    """AJAX"""
    name = 'Dalian'
    allowed_domains = ['dl.gov.cn']
    start_urls = ['http://https://www.dl.gov.cn//']
    api = "https://www.dl.gov.cn/dhc/searchJs/retrieval?question={keyword}&pageNum={page}"
    keywords = ["煤炭"]
    method = "GET"

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data['msg']['list']['全部']['list']
        return items_box

    def edit_page(self, response):
        raw_data = response.json()
        page = raw_data['msg']['list']['全部']['totalPage']
        return int(page)

    def edit_items(self, items_box):
        for item in items_box:
            yield item

    def edit_item(self, item):
        data = {}
        data['title'] = item['xqtitle']
        data['url'] = item['xqurl']
        data['date'] = item['loadtime']
        return data
