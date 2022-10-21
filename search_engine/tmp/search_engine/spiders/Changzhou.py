import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector
from scrapy.shell import inspect_response


class ChangzhouSpider(ZhengFuBaseSpider):
    """DONE"""
    name = '常州'
    allowed_domains = ['changzhou.gov.cn']
    api = "http://search.changzhou.gov.cn/index.php?c=index&a=search&keyword={keyword}&referer=&range=2&edit=0&lanmu=0&sitename=all&sort=3&time=0&page={page}&contype=0"

    method = "GET"

    def edit_items_box(self, response):
        raw_data = response.json()
        raw_html = raw_data["result_html"]
        items_box = Selector(text=raw_html, type="html")
        return items_box

    def edit_items(self, items_box):
        items = []
        items_rec = items_box.css("div.sblock")  # 会有 10 阶，嵌套结构
        rec_deep = len(items_rec)
        for _ in range(rec_deep - 1):
            items.append(self.diff(items_rec[_], items_rec[_ + 1]))
        items.append(items_rec[-1])
        print(items)
        return items

    def edit_item(self, item):
        item_data = {}
        item_data['url'] = item.css("div.dat > a::text").get()
        item_data['source'] = item.css("div.dat::text").re(r'(.*?) - (.*?) - ')[1]
        item_data['date'] = item.css("div.dat::text").re(r'(.*?) - (.*?) - ')[0]
        item_data['title'] = item.css("div.tit > a::text").get()
        item_data['type'] = item.css("div.tit > span::text").get()
        return item_data

    def edit_page(self, response):
        # inspect_response(response, self)
        raw_data = response.json()
        total_item_num = int(raw_data['total'])
        total_page_num = total_item_num // 10
        return total_page_num

    def diff(self, first, second):
        """用于处理嵌套结构差分"""
        len_second = len(second.get())
        html_diff = first.get()[:-len_second]
        return Selector(text=html_diff, type="html")
