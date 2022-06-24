import scrapy
from Hue.basepro import ZhengFuBaseSpider


class WuzhongSpider(ZhengFuBaseSpider):
    name = 'Wuzhong'
    allowed_domains = ['wuzhong.gov.cn']
    start_urls = ['http://http://www.wuzhong.gov.cn//']
    api = "http://www.wuzhong.gov.cn/was5/web/outlinecontent"
    method = "POST"
    data = {
        "page": "{page}",
        "channelid": "294305",
        "searchword": "{keyword}",
        "keyword": "{keyword}",
        "perpage": "10",
        "outlinepage": "10",
        "templet": "result_document.jsp"
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
        data["title"] = item.css("a.js-title::text").get()
        data["url"] = item.css("a.js-title::attr(href)").get().strip()
        data["date"] = item.css("p > span::text").get()
        return data
