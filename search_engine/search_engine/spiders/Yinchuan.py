import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class YinchuanSpider(ZhengFuBaseSpider):
    """反爬, 跳过"""
    name = 'Yinchuan'
    api = "http://www.yinchuan.gov.cn/was5/web/outlinecontent"
    method = "POST"
    data = {
        "page": "{page}",
        "channelid": "232595",
        "searchword": "{keyword}",
        "keyword": "{keyword}",
        "perpage": "10",
        "outlinepage": "10",
        "templet": [
            "yc_content.jsp",
            "yc_content.jsp"
        ]
    }

    def edit_data(self, data, keyword, page):
        data["page"] = str(page)
        data["searchword"] = keyword
        data["keyword"] = keyword
        return data

    def edit_page(self, response):
        total_page_nums = response.css("a.last-page").re("page=(.*)&amp;channelid")[0]
        return int(total_page_nums)

    def edit_items_box(self, response):
        items_box = response.css("div.js-con")
        return items_box

    def edit_item(self, item):
        data = {}
        data["url"] = item.css("a.js-title::attr(href)").get().strip()
        return data
