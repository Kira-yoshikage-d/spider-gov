import time
from typing import Any, Generator, Iterable, List, Optional, Union

from scrapy import Selector
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class A洛阳Spider(ZhengFuBaseSpider):
    name: str = '洛阳'
    api: str = 'https://article.ly.gov.cn/ms-mcms/esArticle/queryEsArticle.do?pageNumber={page}&pageSize=5&keyword={keyword}&dateType=&esType='
    method: str = 'GET'
    debug: bool = False

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        page = response.json()["totalPage"]
        return int(page)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["list"]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        raw_title = Selector(text=item.get("title", "unknow"))
        raw_date = time.localtime(int(item.get("date", 0)) // 1000)
        result = {
            'title': raw_title.css("::text").getall(),
            'url': item.get("url", "unknow"),
            'date': time.strftime("%Y-%m-%d", raw_date),
        }
        return result
