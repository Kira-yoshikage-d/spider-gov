from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A威海Spider(ZhengFuBaseSpider):
    name: str = '威海'
    api: str = 'http://www.weihai.gov.cn/jsearchfront/interfaces/cateSearch.do'
    method: str = 'POST'

    headers: dict[str, str] = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    }

    data: dict[str, Any] = {
        'websiteid': '371000000000000',
        'q': '{keyword}',
        'p': '{page}',
        'pg': 20,
        'cateid': 142,
        'tpl': 1321,
        'checkError': 1,
        'word': '{keyword}'
    }
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        print(response.text)
        total = response.json()["total"]
        return int(total)//20 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["result"]

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return [Selector(text=item) for item in items_box]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("div.jcse-news-title a::text").get().strip(),
            'url': item.css("div.jcse-news-url a::text").get().strip(),
            'source':  item.css("div.jcse-news-title span::text").get(),
            'date': item.css("span.jcse-news-date::text").get()
        }
        return result

