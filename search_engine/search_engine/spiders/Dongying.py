from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class DongyingSpider(ZhengFuBaseSpider):
    name = 'Dongying'
    method = 'POST'
    allowed_domains = ['dongying.gov.cn']
    start_urls = ['http://www.dongying.gov.cn']
    api = 'http://www.dongying.gov.cn/jsearchfront/interfaces/cateSearch.do'
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "websiteid" : "370500000000000",
        "q": "{keyword}",
        "p": "{page}",
        "pg": "20",
        "cateid": "14400",
        "pos": "title,content",
        "pq": "", 
        "oq": "", 
        "eq": "", 
        "begin": "", 
        "end": "", 
        "tpl": "185",
    }


    def edit_data(self, data: dict, keyword: str, page: int) -> dict:
        """
        返回POST数据.
        """
        data["q"] = keyword
        data["p"] = str(page)
        return data

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        page = int(response.json().get("total"))
        return page//20+1


    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        return response.json().get('result')

    def edit_items(self, items_box) -> Selector:
        """
        将目录索引整理为标准迭代器.
        """
        return [Selector(text=item) for item in items_box]

    def edit_item(self, item) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            "url":item.css("div.jcse-news-url > a::text").get(),
            "title":item.css("div.jcse-news-title > a::text").get(),
            "date":item.css("div.jcse-news-abs span::text").get(),
            "source":item.css("div.jcse-news-title > span::text").get()
        }

        return data
