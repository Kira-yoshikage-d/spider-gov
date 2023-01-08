from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A广东省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '广东省生态环境厅'
    api: str = 'http://search.gd.gov.cn/api/search/all'
    method: str = 'POST'
    data: dict[str, Any] = {
      "keywords": "{keyword}",
      "sort": "smart",
      "site_id": "160",
      "range": "site",
      "position": "title",
      "page": "{page}",
      "recommand": 1,
      "gdbsDivision": "440000",
      "gdbsOrgNum": "006940060",
      "service_area": 1
    }
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.json()["data"]["news"]["total"]
        return int(total) // 20 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["data"]["news"]["list"]

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
            'source': item.get("publisher_src", "unknown"),
            'date': item.get("pub_time", "unknown"),
        }
        return result

