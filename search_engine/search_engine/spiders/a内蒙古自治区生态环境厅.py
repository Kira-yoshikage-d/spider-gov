from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A内蒙古自治区生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '内蒙古自治区生态环境厅'
    api: str = 'https://sthjt.nmg.gov.cn/nmsearch/trssearch/searchAll.do?siteId=70&searchTag=all&allKeywords={keyword}&fullKeywords=&orKeywords=&notKeywords=&sort=&position=0&organization=&pageNum={page}&pageSize=10&zcYear=&isAlways=1&fileTag='
    method: str = 'GET'
    data: dict[str, Any] = {}
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

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.get("news_doctitle", "unknown"),
            'url': item.get("docpuburl", "unknown"),
            'source': item.get("sourcename", "unknown"),
            'date': item.get("docpubtime", "unknown"),
        }
        return result

