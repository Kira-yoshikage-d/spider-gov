import scrapy
from Hue.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class ChaoyangSpider(ZhengFuBaseSpider):
    name = 'Chaoyang'
    allowed_domains = ['http://www.chaoyang.gov.cn/']
    api = "http://search.changzhou.gov.cn/index.php?c=index&a=search&keyword={keyword}&referer=&range=2&edit=0&lanmu=0&sitename=all&sort=3&time=0&page={page}&contype=0"

    method = "GET"

    def edit_items_box(self, response):
        raw_data = response.json()
        raw_html = raw_data["result_html"]
        items_box = Selector(text=raw_html, type="html")
        return items_box

    def edit_items(self, items_box):
        return items_box.css("div.sblock")

    def edit_item(self, item):
        pass

    def edit_page(self, response):
        raw_data = response.json()
        total_item_num = int(raw_data['total'])
        total_page_num = total_item_num // 10 + 1
        return total_page_num

