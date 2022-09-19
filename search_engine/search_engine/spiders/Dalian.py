import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class DalianSpider(ZhengFuBaseSpider):
    """AJAX
    TODO crawl"""
    name = '大连'
    allowed_domains = ['dl.gov.cn']
    start_urls = ['http://https://www.dl.gov.cn//']
    api = "https://www.dl.gov.cn/dhc/searchJs/retrieval?question={keyword}&pageNum={page}"
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
        data = {
            'url': item['xqurl'],
            'title': scrapy.Selector(text=item['xqtitle']).css("::text").getall(),
            'date': item['xqpudate'],
            'source': item['lmname'],
            'type': item['sjfl'],
            'content': scrapy.Selector(text=item['xqcontent']).css("::text").getall(),
        }
        data['url'] = item['xqurl']
        return data
