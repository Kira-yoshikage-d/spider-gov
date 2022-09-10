from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class HandanSpider(ZhengFuBaseSpider):
    name: str = 'Handan'
    api: str = 'https://www.hd.gov.cn/was5/web/search?page={page}&channelid=256510&searchword={keyword}&keyword={keyword}&orderby=-DocPubTime&perpage=10&outlinepage=10&searchscope=&timescope=&timescopecolumn=&orderby=-DocPubTime&andsen=&total=&orsen=&exclude='
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        try:
            page = response.css("#column1 > div.outline > div:nth-child(2)::text").re(r"找到相关结果约(\d+)条")[0]
        except:
            page = 0
        return int(page)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        box = response.css("#column1 > div > table > tr > td.searchresult > ol > li")
        return box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("div > a  ::text").getall(),
            'url': item.css("div > a::attr(href)").get(),
            'source': "无",
            'date': item.css("div.pubtime::text").get(),
        }
        return result

