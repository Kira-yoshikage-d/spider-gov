from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy import Selector


class A朔州Spider(ZhengFuBaseSpider):
    name: str = '朔州'
    api: str = 'http://search.shuozhou.gov.cn/search/szgovsearch.jsp'
    method: str = 'POST'
    headers: dict[str, str] = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    data: dict[str, Any] = {
        'sword': '{keyword}',
        'siteid': '4',
        'includesword': '',
        'anywords': '',
        'noword': '',
        'newspage': '1',
        'filepage': '1',
        'govpage': '1',
        'sjpage': '0',
        'bsznage': '0',
        'jdpage': '0',
        'picpage': '1',
        'videopage': '1',
        'otherpage': '{page}',
        'orderby': '1',
        'searchMode': '',
        'timeOption': '',
        'showMode': '0',
        'searchColumn': '',
        'StringEncoding': 'utf-8'
    }

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("dl.search-tool-itemcnt span font::text").get()
        return int(total)//15 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.search-result-cntbox div")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("h3.str-title > a::text").get(),
            'url': item.css("h3.str-title > a::attr(href)").get(),
            'source': item.css("div.rst-ft > span::text").get(),
            'date': item.css("div.rst-ft > span:nth-child(3)::text").get(),
            'type': item.css("h3.str-title > span::text").get()
        }
        return result

