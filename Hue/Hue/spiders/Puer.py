import scrapy
import base64
from Hue.basepro import ZhengFuBaseSpider


class PuerSpider(ZhengFuBaseSpider):
    name = 'Puer'
    allowed_domains = ['puershi.gov.cn']
    start_urls = ['http://http://www.puershi.gov.cn//']
    method = "POST"
    api = "http://www.puershi.gov.cn/zhjsjgy.jsp"
    keywords = ["煤炭"]
    data = {
        "wbtreeid": "1001",
        "keyword": "{keyword}",
        "cc": "W10=",
        "ot": "1",
        "rg": "4",
        "tg": "5",
        "clid": "0",
        "currentnum": "{page}"
    }

    def edit_data(self, data, keyword, page):
        data["currentnum"] = str(page)
        data["keyword"] = base64.b64encode(str(keyword).encode("utf8")).decode()
        self.logger.debug("正在爬取：{} 页".format(page))
        return data

    def edit_page(self, response):
        total_page_num = response.css(".listFrame > tr:nth-child(1) > td:nth-child(1) > a:nth-child(4)").re("共有\n\s*(\d*) 页\xa0\xa0")[0]
        return int(total_page_num)

    def edit_items_box(self, response):
        items_box = response.css("div.searchresultdiv")
        return items_box

    def edit_items(self, items_box):
        # items = items_box.css("div.xwd, div.xwdnei")
        # items_num = len(items)
        # for i in range(items_num/2):
        #     first = items[i>>1]
        #     second = items[i>>1+1]
        #     yield first, second
        items = items_box.css("div.xxgk, div.xwd")
        return items

    def edit_item(self, item):
        cur_class = item.css("::attr(class)").get() + "lf"
        cur_date_class = item.css("::attr(class)").get() + "rr"
        data = {}
        data["title"] = item.css("div."+cur_class+" >a::text").get()
        data["url"] = "http://www.puershi.gov.cn/" + item.css("div."+cur_class+" >a::attr(href)").get()
        data["date"] = item.css("div."+cur_date_class).re("发布时间：(.*)")[0]
        return data


