import scrapy
from Hue.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class JiaxingSpider(ZhengFuBaseSpider):
    name = 'Jiaxing'
    allowed_domains = ['jiaxing.gov.cn', 'zj.gov.cn']
    start_urls = ['http://http://www.jiaxing.gov.cn//']
    api = "http://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do"
    method = "POST"
    data = {
        "websiteid": "330401000000000",
        "pg": "10",
        "p": "{page}",
        "tpl": "2296",
        "Municipal_webid": "330401000000000",
        "Municipal_name": "嘉兴市",
        "isContains": "0",
        "q": "{keyword}",
        "cateid": "658",
        "sortType": "1"
    }

    def edit_data(self, data, keyword, page):
        data["q"] = str(keyword)
        data["word"] = str(keyword)
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
        data["title"] = ''.join([w.strip() for w in item.css("div.jcse-news-title").css("a::text,em::text").getall()])
        try:
            data["url"] = item.css("div.jcse-news-url > a::text").get().strip()
        except:
            data["url"] = None
        try:
            data['date'] = item.css("span.jcse-news-date::text").get().strip()
        except:
            data['date'] = None
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_items_num = raw_data.get("total")
        total_page_num = int(total_items_num) // 12 + 1
        return total_page_num
