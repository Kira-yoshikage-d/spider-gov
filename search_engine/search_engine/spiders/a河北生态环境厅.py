from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A河北生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '河北生态环境厅'
    api: str = 'http://hbepb.hebei.gov.cn/zycms/www/search/fullText/101593488407744s101.do?v=1&channel_id_kt=101%2C10003%2C1041323&title_eq={keyword}&pageIndex={page}'
    method: str = 'GET'
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("div#page_nav_list span b::text").get()
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.cms_search_result li")

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
            'title': item.css("div.ssuo_a a::attr(title)").get(),
            'url': "http://hbepb.hebei.gov.cn" + item.css("div.ssuo_a a::attr(href)").get(),
            'type': item.css("p.search_topic label::text").get(),
            'date': item.css("div.ssuo_bt span::text").get(),
        }
        return result

