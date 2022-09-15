from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class LiaochengSpider(ZhengFuBaseSpider):
    name: str = 'Liaocheng'
    api: str = 'http://www.liaocheng.gov.cn/was5/web/search?page={page}&channelid=287273&searchword={keyword}&keyword={keyword}&perpage=10&outlinepage=10&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        items_num = response.css("div.xw_searchPage div.xw_seCondition p > span:nth-child(1)::text").get()
        return int(items_num) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        box = response.css("div#xw_reLeftList > ul.xw_webSe > li")
        return box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("a > h2::text").get(),
            'url': item.css("a::attr(href)").get(),
            'source': "无",
            'date': item.css("a > p:nth-child(3) > span::text").get(),
        }
        return result

