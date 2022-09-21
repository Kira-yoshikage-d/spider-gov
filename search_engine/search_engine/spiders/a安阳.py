from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A安阳Spider(ZhengFuBaseSpider):
    name: str = '安阳'
    api: str = 'https://searchapi.anyang.gov.cn/open/api/external?keywords={keyword}&siteId=4550000372&allKeyword=&anyKeyword=&noKeyword=&searchRange=-1000&sortType=150&beginTime=&endTime=&pageNumber={page}&pageSize=15&fileType=0&docType=0'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        data = response.json()
        total = data['data']['totalPage']
        return int(total)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        data = response.json()
        return data['data']['datas']

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': Selector(text=item['title']).css("  ::text").getall(),
            'url': item['selfUrl'],
            'source': item['content_orgName'],
            'date': item['source'],
            'type': item['type'],
        }
        return result

