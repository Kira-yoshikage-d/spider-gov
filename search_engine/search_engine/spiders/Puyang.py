from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class PuyangSpider(ZhengFuBaseSpider):
    name: str = '濮阳'
    api: str = 'http://www.puyang.gov.cn/zwxx/zwxx_search.asp?words={keyword}&token={token}&dtime={timestamp}&page={page}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = True


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("div.jsearch-info-box > span::text").get()
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div#jsearch-result-items div.jsearch-result-box")

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
            "title": item.css("div.jsearch-result-title a::text").get(),
            "url": item.css("div.jsearch-result-title a::attr(href)").get(),
            "date": item.css("div.jsearch-result-abs-content span::text").get()
        }
        return result

