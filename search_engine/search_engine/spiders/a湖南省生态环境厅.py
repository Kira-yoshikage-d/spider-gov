from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A湖南省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '湖南省生态环境厅'
    api: str = 'http://searching.hunan.gov.cn/hunan/115000000/news?q={keyword}&searchfields=&sm=0&columnCN=&iszq=&aggr_iszq=&p={page}&timetype=timeqb'
    method: str = 'GET'
    data: dict[str, Any] = {}
    start_page: int = 0
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("div.choose div.time-limit p").re("\d+")[0]
        return int(total) // 9 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.main-content div#hits li")

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
            'title': item.css("div.com-title a::attr(title)").get(),
            'url': item.css("div.com-title a::attr(href)").get(),
            'source': item.css("div.right span.source-name::text").get(),
            'date': item.css("div.right span.source-time::text").get(),
        }
        return result

