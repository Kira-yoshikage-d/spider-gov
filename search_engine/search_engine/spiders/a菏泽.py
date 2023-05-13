from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A菏泽Spider(ZhengFuBaseSpider):
    # 爬不到链接
    name: str = '菏泽'
    api: str = 'http://www.heze.gov.cn/els-service/search/{page}/10'
    method: str = 'POST'
    data: dict[str, Any] = {
        "dq": "0530",
        "fwzt": 3,
        "highlight": "1",
        "isSearch": "1",
        "subject": "{keyword}",
    }
    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
    }
    json_mode = True
    debug: bool = True

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        return int(response.json()["data"]["totalPages"])

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["data"]['contents']

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
            'title': item.get("subject",""),
            'url': item.get("url","")
        }
        return result

