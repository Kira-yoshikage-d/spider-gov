from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class HezeSpider(ZhengFuBaseSpider):
    name: str = '菏泽'
    api: str = 'http://www.heze.gov.cn/jsearchfront/interfaces/cateSearch.do'
    method: str = 'POST'
    data: dict[str, Any] = {
        "websiteid": "371700000000000",
        "q": "{keyword}",
        "p": "{page}",
        "pg": "20",
        "cateid": "14491",
        "pos": "",
        "pq": "",
        "oq": "",
        "eq": "",
        "begin": "",
        "end": "",
        "tpl": "27",
    }
    headers: dict[str, str] = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
    }
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        data = response.json()
        page = data["total"]
        return int(page) // 20 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        data = response.json()
        return data["result"]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        s = Selector(text=item)
        result = {
            'title': s.css("div.jcse-news-title > a::text").get(),
            'url': s.css("div.jcse-news-abs div.jcse-news-url a::text").get(),
            'source': s.css("div.jcse-news-title > span::text").get(),
            'date': s.css("div.jcse-news-other-info span.jcse-news-date::text").get(),
        }
        return result

