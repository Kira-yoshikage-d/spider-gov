from typing import Any, Generator, Iterable, List, Optional, Union
from functools import reduce

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A张家口Spider(ZhengFuBaseSpider):
    name: str = '张家口'
    api: str = 'https://www.zjk.gov.cn/tseach/searchKeywords?keyword={keyword}&fieldSt=1&size=20&startTime=&endTime=&pid=&p={page}&classId=&siteId=1'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        data = response.json()
        total = data['data']['infos']['totalPages']
        return int(total)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        data = response.json()
        return data['data']['infos']['content']

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': Selector(text=item['content_title']).css("  ::text").getall(),
            'url': item['content_pageUrl'],
            'source': item['content_orgName'],
            'date': item['content_addTime'],
            'type': item['content_className'],
        }
        return result

