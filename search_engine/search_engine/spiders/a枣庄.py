from typing import Any, Generator, Iterable, List, Optional, Union

from scrapy import Selector
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class A枣庄Spider(ZhengFuBaseSpider):
    name: str = '枣庄'
    api: str = 'http://www.zaozhuang.gov.cn/was5/web/search?page={page}&channelid=232389&searchword={keyword}&keyword={keyword}&orderby=-DOCRELTIME&perpage=10&outlinepage=10&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME'
    method: str = 'GET'
    debug: bool = False

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("div.xw_seCondition span::text").get()
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.xw_reLeft ul li")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'url': item.css("a::attr(href)").get(),
            'title': item.css("h2::text").get(),
            'date': item.css("span::text").re("发布时间：(.*)")[0],
        }
        return result
