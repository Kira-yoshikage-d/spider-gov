from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A新乡Spider(ZhengFuBaseSpider):
    name: str = '新乡'
    api: str = 'http://www.xinxiang.gov.cn/search/SolrSearch/s'
    method: str = 'POST'
    data: dict[str, Any] = {
        'token4': 'f0d933a8a9e247118bacc5cc8eed50e2',
        'q': '{keyword}',
        'articlePublishTimeStart': '',
        'articlePublishTimeEnd': '',
        'siteId': '641a8f75d6d44ac09a68afc6aae73c23',
        'rows': '10',
        'page': '{page}',
        'catalogLevel': '',
        'type': ''
    }
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("h4 small::text").re("共*([0-9]*)条")[0]
        return int(total)//10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.media")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': ''.join(item.css("h4 a::text").getall()),
            'url': "http://www.xinxiang.gov.cn/" + item.css("h4 a::attr(href)").get(),
            'date': item.css("div.result-inner i::text").get().split(":")[1],
        }
        return result

