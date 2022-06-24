import scrapy
from Hue.basepro import ZhengFuBaseSpider


class ZhongshanSpider(ZhengFuBaseSpider):
    name = 'Zhongshan'
    allowed_domains = ['zs.gov.cn', 'gd.gov.cn']
    start_urls = ['http://http://www.zs.gov.cn//']
    api = "http://search.gd.gov.cn/api/search/all"
    method = "POST"
    data = {
        "gdbsDivision": "442000",
        "keywords": "{keyword}",
        "page": "{page}",
        "position": "title",
        "range": "site",
        "recommand": "1",
        "service_area": "760",
        "site_id": "760001",
        "sort": "smart"
    }

    def edit_data(self, data, keyword, page):
        data["keywords"] = str(keyword)
        data["page"] = str(page)
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_items_num = raw_data["data"]["news"]["total"]
        total_page_num = int(total_items_num) // 20 + 1
        return total_page_num

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data["data"]["news"]["list"]
        return items_box

    def edit_item(self, item):
        data = {}
        data["title"] = item.get("title", None)
        data["url"] = item.get("url", None)
        data["date"] = item.get("pub_time", None)
        return data
