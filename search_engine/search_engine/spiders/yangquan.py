from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class YangquanSpider(ZhengFuBaseSpider):
    name = 'Yangquan'
    api = 'http://www.yq.gov.cn/search/yqsearch.jsp'
    method = 'POST'
    debug = False
    headers: dict[str, str] = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Referer": "http://www.yq.gov.cn/search/yqsearch.jsp"
    }
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
        page = response.css('div.sresult-flag-cntbox:not(.hide)   span.shanxi-gov-page-form::text').re('共(\d+)页')[0]
        return int(page)

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
        frame = response.css("div.sresult-flag-cntbox:not(.hide)")
        return frame.css("div.search-result-cntbox > div.srt-container")

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        result = {
            'title': item.css("h3.srt-title > a::text").getall(),
            'url': item.css("h3.srt-title > a::attr(href)").get(),
            'source': item.css("div.rst-ft > span:nth-child(1)::text").get(),
            'date': item.css("div.rst-ft > span:nth-child(3)::text").get(),
        }
        return result
