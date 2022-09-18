import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class JinhuaSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '金华'
    api = "https://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do"
    method = "POST"
    data = {
        "websiteid": "330701000000000",
        "tpl": "2296",
        "Municipal_webid": "330701000000000",
        "Municipal_name": "金华市",
        "isContains": "1",
        "q": "{keyword}",
        "p": "{page}",
        "cateid": "370",
        "pg": "10",
        "sortType": "1"
    }

    def edit_data(self, data, keyword, page):
        data["q"] = str(keyword)
        data["p"] = str(page)
        return data

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data["result"]
        return items_box

    def edit_items(self, items_box):
        items = [Selector(text=item, type="html") for item in items_box]
        return items

    def edit_item(self, item):
        data = {}
        try:
            data["url"] = item.css("div.jcse-news-title > a::attr(href)").get().strip()
        except:
            data["url"] = ""
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_items_num = raw_data.get("total")
        total_page_num = int(total_items_num) // 10 + 1
        return total_page_num
