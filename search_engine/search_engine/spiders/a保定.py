from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A保定Spider(ZhengFuBaseSpider):
    name: str = '保定'
    api: str = 'http://www.baoding.gov.cn/index.do?view=search&fields=title,title2,summary,contents&keyword={keyword}&page={page}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("body > div.main > table > tbody > tr > td.ej_rbr > div:nth-child(2) > table > tr:nth-child(1) > td:nth-child(2)::text").re("：(.*)条")[0]
        return int(total) // 20 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("body > div.main > table > tbody > tr > td.ej_rbr > div:nth-child(2) > table a")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("::text").get(),
            'url': 'http://www.baoding.gov.cn/' + item.css("::attr(href)").get(),
            'source': '无',
            'date': '无',
        }
        return result

