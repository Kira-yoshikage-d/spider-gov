from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A天津生态环境局Spider(ZhengFuBaseSpider):
    name: str = '天津生态环境局'
    api: str = 'https://sthj.tj.gov.cn/igs/front/search.jhtml?code=83ad3975ebda482887112716b970bee5&pageNumber={page}&pageSize=10&queryAll=true&searchWord={keyword}&siteId=59'
    method: str = 'GET'
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        page = response.json()["page"]["totalPages"]
        return int(page)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["page"]["content"]

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
            'title': item.get("title", "none"),
            'url': item.get("url", "none"),
            'type': item.get("trs_type", "none"),
            'date': item.get("trs_time", "none"),
        }
        return result

