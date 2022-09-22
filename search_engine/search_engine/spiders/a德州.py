from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A德州Spider(ZhengFuBaseSpider):
    name: str = '德州'
    api: str = 'http://www.dezhou.gov.cn/searchweb/search?page={page}&channelid=275584&searchword={keyword}&keyword={keyword}&perpage=10&outlinepage=10&&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=%2BSITEID%2C-PUBLISH_TIME'
    method: str = 'GET'
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("div.left div.result p span::text").get()
        return int(total)//10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.serach_result_list > ul > li")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("h2 a::text").get(),
            'url':  item.css("h2 a::attr(href)").get(),
            'source': item.css("h2 span::text").get(),
            'date': item.css("span.link::text").re("：(.*)"),
        }
        return result

