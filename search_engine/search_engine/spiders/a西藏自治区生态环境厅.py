from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A西藏自治区生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '西藏自治区生态环境厅'
    api: str = 'http://ee.xizang.gov.cn/igs/front/search.jhtml?code=6af1a49b742b4dfeb151891aaddf208b&pageNumber={page}&pageSize=10&searchWord={keyword}&siteId=48'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        return int(response.json()["page"].get("totalPages", "0"))

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
            'title': item.get("title", "unknown"),
            'url': item.get("url", "unknown"),
            'type': item.get("trs_type", "unknown"),
            'source': item.get("trs_site", "unknown"),
            'date': item.get("trs_time", "unknown"),
        }
        return result

