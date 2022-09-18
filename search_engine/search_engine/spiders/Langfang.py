from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class LangfangSpider(ZhengFuBaseSpider):
    name: str = 'Langfang'
    api: str = 'http://www.lf.gov.cn/search.aspx?fieldOption=title&modelID=0&searchType=0&keyword={keyword}&page={page}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("#pe100_page_全站搜索按标题_普通式 > span::text").get()
        return int(total)//200 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("#content > div.listContent > div.mainContent > ul > li")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("a.tit::attr(title)").get(),
            'url': 'http://www.lf.gov.cn' + item.css("a.tit::attr(href)").get(),
            'source': item.css("a.node::text").get(),
            'date': item.css("span.date::text").get(),
        }
        return result

