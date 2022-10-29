from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class XinjiSpider(ZhengFuBaseSpider):
    name: str = '辛集'
    api: str = 'https://www.xinji.gov.cn/search?q={keyword}&page={page}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        page = response.css("#pagenav > span::text").re(r"共 (\d+) 条")[0]
        return int(page) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        box = response.css("#apple > li")
        return box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("h3.sr-title a::text").getall(),
            'url': 'https://www.xinji.gov.cn' + item.css("h3.sr-title a::attr(href)").get(),
            'date': item.css("div.sr-footer > span:nth-child(1)::text").get(),
            'source': '-'.join(item.css("div.sr-footer a::text").getall()),
        }
        return result

