from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A开封Spider(ZhengFuBaseSpider):
    name: str = '开封'
    api: str = 'https://www.kaifeng.gov.cn/searchEngine.do?offset={page}'
    method: str = 'POST'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data: dict[str, Any] = {
        'siteidIndex': '402881fa2194c26c012194c38dc80001',
        'cacnameIndex': '',
        'cicontentIndex': "{keyword}",
        "cacidIndex": "",
        "caclevelIndex": "",
        "cicreatetime": "",
        "typeIndex": "",
        "cititleIndex": "{keyword}",
        "cikeyIndex": "{keyword}"
    }
    debug: bool = False
    start_page = 0


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("strong::text")[-1].get()
        return int(total) // 15 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("td[valign='top'][height='30']")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("a::text").get(),
            'url': item.css("a::attr(href)").get(),
            'source': item.css("p::text").get(),
            'date': item.css("a.green::text").get(),
        }
        return result

