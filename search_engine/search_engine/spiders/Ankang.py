from Hue.basepro import ZhengFuBaseSpider
from scrapy import Selector
from scrapy.responsetypes import Response


class AnkangSpider(ZhengFuBaseSpider):
    """DONE"""

    name = 'Ankang'
    api = "https://so.ankang.gov.cn/s?t=0&s=0&sid=0&n=&q={keyword}&i=7&ctype=7&ft=0&date=&day=&p={page}"
    method = "GET"

    def edit_page(self, response: Response):
        try:
            total_item_num = response.css(
                "#content > div.soujieguo > div.souJg::text").re(
                    r'.*为您找到(\d*)条信息.*')[0]
        except Exception:
            return 0
        return (int(total_item_num) // 20 + 1)

    def edit_items_box(self, response: Response):
        items_box = response.css("#content > ul > li")
        return items_box

    def edit_item(self, item: Selector):
        try:
            url = item.css("em:nth-child(4)::text").re(r'链接：(.*)$')[0]
        except Exception:
            url = ""
        return {"url": url}
