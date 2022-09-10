from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class YangquanSpider(ZhengFuBaseSpider):
    name = 'yangquan'
    api = 'http://www.yq.gov.cn/search/yqsearch.jsp'
    method = 'POST'
    data = {
        "sword": "{keyword}",
        "newspage": "1",
        "filepage": "1",
        "govpage": "1",
        "picpage": "1",
        "videopage": "1",
        "otherpage": "{page}",
        "orderby": "2",
        "searchMode": "",
        "showMode": "0",
        "searchColumn": "",
        "StringEncoding": "utf-8",
    }

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        item_num = int(response.css("li.tab-current > em::text").re("\((\d+)\)")[0])
        return item_num // 15 + 1

    def edit_data(self, data: dict, keyword: str, page: int) -> dict:
        """
        返回POST数据.
        """
        data["sword"] = keyword
        data["otherpage"] = str(page)
        return data

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        return response.css("div.search-result-cntbox > div.srt-container")

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        result = {
            'title': ''.join(response.css("h3.srt-title::text").getall()),
            'url': response.css("h3.srt-title > a::attr(href)").get(),
            'source': response.css("div.rst-ft > span:nth-child(1)::text").get(),
            'date': response.css("div.rst-ft > span:nth-child(3)::text").get(),
        }
        return result
