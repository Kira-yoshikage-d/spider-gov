import scrapy
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class WeifangSpider(ZhengFuBaseSpider):
    """TODO 看上去有点麻烦"""
    name = '潍坊'
    api = "http://search.shandong.gov.cn/search"
    method = "POST"
    data = {
        "pageNo": "{page}",
        "pageSize": "10",
        "category2": "370700000000",
        "category4": "",
        "category5": "",
        "accurateMode": "",
        "channel2": "一网通办",
        "category9": "",
        "site": "all",
        "text": "{keyword}",
        "category1": "",
        "category3": "",
        "topicType": "",
        "sortMode": "",
        "searchMode": "",
        "timeRange": "",
        "channel1": "",
        "totalSize": "140",
        "QTime": "205",
        "accurateWord": "",
        "sourceWord": "{keyword}",
    }

    def edit_data(self, data: dict, keyword: str, page: int):
        data["text"] = keyword
        data["sourceWord"] = keyword
        data["pageNo"] = str(page)
        return data

    def edit_items_box(self, response: Response):
        return response.css("div.result-op")

    def edit_item(self, item):
        result = {}
        result["url"] = item.css("div.r-i-til > a.wl-item::attr(href)").get()
        return result

    def edit_page(self, response: Response) -> int:
        try:
            total_num = int(response.css("#totalSizeSpan::text").get())
        except Exception:
            total_num = 0
        return total_num // 10 + 1


