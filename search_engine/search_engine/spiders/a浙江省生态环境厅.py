from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A浙江省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '浙江省生态环境厅'
    api: str = 'https://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do'
    method: str = 'POST'
    data: dict[str, Any] = {
        "websiteid": "330000000000015",
        "tpl": "2330",
        "q": "{keyword}",
        "imageField.x": "0",
        "imageField.y": "0",
        "p": "{page}",
        "cateid": "370",
        "pg": "10",
        "sortType": "1",
        "pos": "filenumber, title, content, keyword"
    }
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.json()["total"]
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()['result']

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
            'title': item.css("div.jcse-news-title a::text").get(),
            'url': "https://search.zj.gov.cn/jrobotfront/" + item.css("div.jcse-news-title a::attr(href)").get(),
            'source': item.css("div.website-source span.jcse-news-date2::text").get(),
            'date': item.css("div.website-source span.jcse-news-date1::text").get(),
            'type': item.css("div.jcse-news-title span.typeTtitle::text").get()
        }
        return result

