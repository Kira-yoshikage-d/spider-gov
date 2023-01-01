from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A辽宁省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '辽宁省生态环境厅'
    api: str = 'http://www.ln.gov.cn/was5/web/search?page={page}&channelid=297510&searchword={keyword}&keyword={keyword}&StringEncoding=UTF-8&was_custom_expr=doctitle%3D%28{keyword}%29&perpage=10&outlinepage=10'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("ul.cx_ul li#one4 span::text").re("\(([0-9]*)")[0]
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.cx_cont ul li")

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
            'title': item.css("a::text").getall(),
            'url': item.css("a::attr(href)").get(),
            'date': item.css("span::text").get(),
        }
        return result

