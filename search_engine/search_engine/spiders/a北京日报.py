from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A北京日报Spider(ZhengFuBaseSpider):
    name: str = '北京日报'
    api: str = 'https://s.bjd.com.cn/api/search/get?page={page}&keyboard={keyword}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        return 500

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()['data']['data']

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.get("title", "无"),
            'url': item.get("befrom_url", "无"),
            'source': item.get("befrom", "无"),
            'date': item.get("issue_time", "无"),
        }
        return result

