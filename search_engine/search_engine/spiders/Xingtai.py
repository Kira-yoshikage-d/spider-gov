from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class XingtaiSpider(ZhengFuBaseSpider):
    name: str = '邢台'
    api: str = 'http://www.xingtai.gov.cn/was5/web/search?page={page}&channelid=234439&searchword={keyword}&keyword={keyword}&perpage=10&outlinepage=10&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        page = response.css("p.tiaoshutle > span::text").get()
        return int(page) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        box = response.css("dl.list_qwjsgaoji")
        return box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("dt > a::text").get(),
            'url': item.css("dt > a::attr(href)").re(r"'(.*?')")[0],
            'source': "无",
            'date': item.css("p::text").get(),
        }
        return result

