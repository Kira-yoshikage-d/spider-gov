from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A新疆生产建设兵团生态环境局Spider(ZhengFuBaseSpider):
    name: str = '新疆生产建设兵团生态环境局'
    api: str = 'http://sthjj.xjbt.gov.cn/zcms/front/search/advances?query={keyword}&siteID=403&sort=publishDate&pageIndex={page}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False
    start_page: int = 0


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.json()["data"]["total"]
        return int(total) // 20 + 1

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
            'title': item.get("title", "unknown"),
            'url': item.get("url", "unknown"),
            'source': item.get("source", "unknown"),
            'date': item.get("publishDate", "unknown"),
            'type': item.get("catalogName", "unknown")
        }
        return result

