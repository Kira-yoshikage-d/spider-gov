import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy import Request


class NanjingSpider(ZhengFuBaseSpider):
    """ Ajax
    TODO crawl"""
    name = '南京'
    api = "https://www.nanjing.gov.cn/igs/front/search.jhtml?code=c1c8a0a187b3404a9e7e1b048f90610c&pageSize=10&searchWord={keyword}&searchWord2={keyword}&siteId=10&pageNumber={page}"
    method = "GET"
    debug = True

    def edit_items_box(self, response):
        box = response.json()
        items_box = box['page']
        return items_box

    def edit_items(self, items_box):
        for item in items_box['content']:
            yield item

    def edit_item(self, item):
        result = {}
        result['url'] = item.get('url', '')
        result['date'] = item.get('docreltime', '')
        result['source'] = item.get('trs_site', '')
        result['type'] = item.get('trs_type', '')
        result['title'] = item.get('title', '').replace("<em>","")

        return result


    def edit_page(self, response):
        raw_data = response.json()
        return raw_data['page']['totalPages']
