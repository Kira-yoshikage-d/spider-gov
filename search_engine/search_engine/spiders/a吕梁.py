from typing import Any, Generator, Iterable, List, Optional, Union

from scrapy import Selector
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class A吕梁Spider(ZhengFuBaseSpider):
    name: str = '吕梁'
    api: str = 'http://www.lvliang.gov.cn/trs-search/trssearch/v2/searchAll.do?siteId=5&searchTag=all&allKeywords={keyword}&fullKeywords=&orKeywords=&notKeywords=&sort=time&position=0&organization=&pageNum={page}&pageSize=10&zcYear=&isAlways=1&fileTag='
    method: str = 'GET'
    debug: bool = False

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.json()["data"]["total"]
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["data"]["data"]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.get("title", "无"),
            'url': item.get("docpuburl", "无"),
            'source': item.get("sourcename", "无"),
            'date': item.get("docpubtime", "无"),
            'type': item.get("chnldesc", "无")
        }
        return result
