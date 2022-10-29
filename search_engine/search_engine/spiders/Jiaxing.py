import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class JiaxingSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '嘉兴'
    api = "https://search.zj.gov.cn/jsearchfront/interfaces/new_zwfw.do"
    method = "POST"
    data = {
        "usePinYinCorrect": "true",
        "pageSize": "10",
        "word": "{keyword}",
        "regionCode": "330401",
        "current": "{page}"
    }

    def edit_data(self, data, keyword, page):
        data["word"] = str(keyword)
        data["current"] = str(page)
        return data

    def edit_items_box(self, response):
        raw_data = response.json()
        return raw_data.get('data').get('list')

    def edit_item(self, item):
        data = {}
        code = item.get('data').get('sourceDocId')
        data['url'] = "https://www.zjzwfw.gov.cn/zjservice/item/detail/index.do?localInnerCode={}".format(code)
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_page_num = raw_data.get("totalPages", 0)
        return int(total_page_num)
