from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A吉林省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '吉林省生态环境厅'
    api: str = 'http://was.jl.gov.cn/was5/web/search?page={page}&channelid=265558&searchword={keyword}&keyword={keyword}&StringEncoding=UTF-8&perpage=10&outlinepage=10&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=-DATETIME'
    method: str = 'GET'
    data: dict[str, Any] = {}
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    cookie = "bgm=1; JSESSIONID=6D6622603907F51A5B823D226D87596E; _trs_uv=lck5q9vf_1090_gflf; wzws_sessionid=oGQeSdCBNjIwZWVhgDI0MGU6NDY0OjI1MTA6MWZlMDo4ZGYwOjcyYjY6M2YxNTo2MmKCZDc2OWM0"
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("div.toolsnav span.nums::text").re("\d+")[0]
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.sub_bg_white_box dl")

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
            'title': item.css("a::text").get(),
            'url': item.css("a::attr(href)").get(),
            'date': item.css("dd::text").re("发布时间：(.+)")[0],
        }
        return result

