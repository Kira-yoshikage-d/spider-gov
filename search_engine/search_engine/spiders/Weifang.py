import scrapy
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class WeifangSpider(ZhengFuBaseSpider):
    """TODO 看上去有点麻烦"""
    name = '潍坊'
    api = "http://search.shandong.gov.cn/api/search"
    method = "POST"
    data ={
        "q": "{keyword}",
        "regionCode": "",
        "channel": "1",
        "correctionNegative": "null",
        "searchRecordId": "c4993d1c-a8ba-473e-8367-9356ed374184",
        "site": "local",
        "page": "{page}",
        "itemType": "",
        "itemPeopleTopic": "",
        "itemCompanyTopic": "",
        "newsCatalog": [],
        "orderMode": "",
        "timeRange": "",
        "debug": "null"
    }
    json_mode = True
    debug = False

    def edit_items_box(self, response: Response):
        return response.json()["data"]["elements"]

    def edit_item(self, item):
        result = {}
        result["title"] = item.get("resourceTitle","")
        return result

    def edit_page(self, response: Response) -> int:

        total = response.json()["data"]["totalHits"]
        return int(total) // 10 + 1


