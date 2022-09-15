from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class PuyangSpider(ZhengFuBaseSpider):
    name: str = 'Puyang'
    api: str = 'http://www.puyang.gov.cn/zwxx/zwxx_search.asp?words={keyword}&bianhao=%C7%EB%CA%E4%C8%EB%CE%C4%BA%C5&nian=&wenzhong=0&token=1662895891&page={page}'
    method: str = 'default'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        raise NotImplementedError()

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        raise NotImplementedError()

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
        }
        return result

