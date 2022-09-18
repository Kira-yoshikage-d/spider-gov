import scrapy
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class QuzhouSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '衢州'
    allowed_domains = ['qz.gov.cn', 'zj.gov.cn']
    start_urls = ['http://http://www.qz.gov.cn//']
    api = "https://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do"
    method = "POST"
    data = {
        "q": "{keyword}",
        "websiteid": "330801000000000",
        "pg": "10",
        "tpl": "2296",
        "Municipal_webid": "330801000000000",
        "cateid": "370",
        "sortType": "1",
        "p": "{page}"
    }

    def edit_data(self, data: dict, keyword: str, page: int):
        data["q"] = keyword
        data["p"] = str(page)
        return data

    def edit_page(self, response: Response) -> int:
        total_num = int( response.json().get("total") )
        return total_num // 10 + 1

    def edit_items_box(self, response: Response):
        return response.json().get('result')

    def edit_items(self, items_box):
        return [Selector(text=item) for item in items_box]

    def edit_item(self, item):
        data = {}
        data['url'] = item.css("div.jcse-news-title > a::attr(href)").get()
        return data


