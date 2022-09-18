from typing import Any, Generator, Iterable, List, Optional, Union
import json

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class QinhuangdaoSpider(ZhengFuBaseSpider):
    name: str = '秦皇岛'
    api: str = 'http://www.qhd.gov.cn/front_searchall.do?state=&pn={page}&pageSize=10&query={keyword}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        data = response.json()
        data = json.loads(data['news'])
        return int(data['pages'])

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        data = response.json()
        data = json.loads(data['news'])
        return data['result']

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item['title'],
            'date': item['inserttime'],
            'source': item['come_from'],
            'url': 'http://www.qhd.gov.cn/front_pcthi.do?uuid=' + item['uuid'],
        }
        return result

