import scrapy
from Hue.basepro import ZhengFuBaseSpider


class ChenzhouSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = 'Chenzhou'
    allowed_domains = ['czs.gov.cn', 'hunan.gov.cn']
    api = "http://searching.hunan.gov.cn:8977/hunan/980000000/news?q={keyword}&searchfields=&sm=0&columnCN=&iszq=&aggr_iszq=&p={page}&timetype=timeqb"
    method = "GET"
    start_page = 0

    def edit_page(self, response):
        total_items_num = response.css("div.time-limit.result").re("相关结果约(.*)个")[0]
        total_page_num = int(total_items_num) // 10 + 1
        return total_page_num

    def edit_items_box(self, response):
        items_box = response.css("div#hits")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("li")
        return items

    def edit_item(self, item):
        data = {}
        data["url"] = item.css("div.title > a::attr(href)").get()
        return data
