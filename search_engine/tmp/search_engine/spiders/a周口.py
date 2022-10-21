from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A周口Spider(ZhengFuBaseSpider):
    name: str = '周口'
    api: str = 'http://www.zhoukou.gov.cn/search/SolrSearch/searchData'
    method: str = 'POST'
    data: dict[str, Any] = {
        'q': '{keyword}',
        'type': '',
        'timeType': '',
        'sort': '',
        'order': '',
        'forCatalogType': '0',
        'token4': '1a1365d6d0d64a00b074d6131acb1860',
        'siteId': '9752499e88b94e1881e46bbeeef1376e',
        'offset': '{page}',
        'limit': '10',
        'infoType': ''
    }
    debug: bool = False

    def edit_data(self, data: dict, keyword: str, page: int, **kwargs) -> dict[str, Any]:
        data['offset'] = (page-1)*10
        return data

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        return int(response.json()['totalPage'])

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()['rows']

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            "title": item.get("articleTitle", ""),
            "url": "http://www.zhoukou.gov.cn" + item.get("articleUri", ""),
            "date": item.get("articlePublishTime", ""),
            "source": item.get("siteName", ""),
        }
        return result

