import scrapy
from Hue.basepro import ZhengFuBaseSpider


class FuzhouSpider(ZhengFuBaseSpider):
    name = 'Fuzhou'
    allowed_domains = ['jxfz.gov.cn']
    start_urls = ['http://http://www.jxfz.gov.cn//']
    api = "http://www.jxfz.gov.cn/jrobot/search.do?webid=1&pg=12&p={page}&tpl=&category=&q={keyword}&pos=title,content&od=&date=,"
    method = "GET"
    keywords = ["煤炭"]

    def edit_page(self, response):
        total_items_nums = response.css("div.jsearch-info-box::attr(data-total)").get()
        total_page_nums = int(total_items_nums) // 12 + 1
        return total_page_nums

    def edit_items_box(self, response):
        items_box = response.css("div#jsearch-result-items")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("div.jsearch-result-box")
        return items

    def edit_item(self, item):
        data = {}
        data["title"] = item.css("div.jsearch-result-title > a::text").get()
        data["url"] = item.css("div.jsearch-result-title > a::attr(href)").get()
        data["date"] = item.css("span.jsearch-result-date").get()
        return data

