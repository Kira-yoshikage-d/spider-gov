from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A忻州Spider(ZhengFuBaseSpider):
    name: str = '忻州'
    api: str = 'https://www.sxxz.gov.cn/was5/web/search?searchscope=&timescope=&timescopecolumn=docreltime&orderby=-docreltime&channelid=260481&andsen=&total=&orsen=&exclude=&lanmu=&page={page}&searchword={keyword}&perpage=&token=&templet='
    method: str = 'GET'
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("ul.search-show-cnt li.resul-tt-font span::text").get()
        return int(total)//10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.search-result-inner-box dl")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("dt a::attr(title)").get(),
            'url':  item.css("dt a::attr(href)").get(),
            'source': item.css("dd div::text").get(),
            'date': item.css("dd span::text").get(),
        }
        return result

