from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A晋中Spider(ZhengFuBaseSpider):
    name: str = '晋中'
    api: str = 'https://www.sxjz.gov.cn/s?sid=0&wd={keyword}&p={page}&vc='
    method: str = 'GET'
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        page = response.css("div.pager span").re("/共(.*?)页")[0]
        return int(page)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.result-list.article ul li")

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
            'title': item.css("h4 a::text,h4 span::text").getall(),
            'url': item.css("h4 a::attr(href)").get(),
            'source': item.css("div.attribution span::text").re("来源：(.*)")[0],
            'date': item.css("div.attribution::text").re(r"\d{4}/\d{1,2}/\d{1,2}")[0],
            'type': item.css("span::text").get()
        }
        return result

