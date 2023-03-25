from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import json


class A福建省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '福建省生态环境厅'
    api: str = 'http://sthjt.fujian.gov.cn/was5/web/search?channelid=229105%2C242992&templet=advsch.jsp&sortfield=-docreltime&classsql=(siteid%3D8)*({keyword})&prepage=50&page={page}'
    method: str = 'GET'
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        res = json.loads(response.text.replace("\n", ""))
        total = res["count"]
        return int(total) // 50 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        res = json.loads(response.text.replace("\n", ""))
        return res["docs"]

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
            'title': item.get("title","unknown"),
            'url': item.get("url","unknown"),
            'source': item.get("src","unknown"),
            'date': item.get("pubtime","unknown"),
        }
        return result

