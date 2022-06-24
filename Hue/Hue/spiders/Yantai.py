import scrapy
from Hue.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class YantaiSpider(ZhengFuBaseSpider):
    name = 'Yantai'
    allowed_domains = ['yantai.gov.cn']
    start_urls = ['http://http://www.yantai.gov.cn//']
    api = "http://www.yantai.gov.cn/jsearchfront/interfaces/cateSearch.do"
    method = "POST"
    data = {
        "websiteid": "370600000000000",
        "q": "{keyword}",
        "p": "{page}",
        "pg": "20",
        "cateid": "5",
        "pos": "",
        "pq": "",
        "oq": "",
        "eq": "",
        "begin": "",
        "end": "",
        "tpl": "82",
        "sortFields": ""
    }

    def edit_data(self, data, keyword, page):
        data["q"] = str(keyword)
        data["p"] = str(page)
        return data

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data.get("result", None)
        return items_box

    def edit_items(self, items_box):
        items = [Selector(text=item, type="html") for item in items_box]
        return items

    def edit_item(self, item):
        data = {}
        data["title"] = ''.join([w.strip() for w in item.css("div.jcse-news-title").css("a::text,em::text").getall()])
        data['url'] = item.css("div.jcse-news-title a::attr(href)").get()
        data['date'] = item.css("span.jcse-news-date::text").get()
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_items_num = raw_data.get("total", 0)
        total_page_num = int(total_items_num) // 20 + 1
        return total_page_num
