from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy import Selector
import time


class A滨州Spider(ZhengFuBaseSpider):
    name: str = '滨州'
    api: str = 'http://60.215.8.10:9027/zfxxgk/api/news/listQuery?column=fbdate&order=desc&jgid=&syh=371601&titleLike={keyword}&bodyLike=&fbdateBegin=&fbdateEnd=&cwbdateBegin=&cwbdateEnd=&yxx=&gwzl=&pageSize=20&pageNo={page}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        page = response.json()['result']['pages']
        return int(page)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()['result']['records']

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item['title'],
            'url': 'http://www.binzhou.gov.cn/zfxxgk/news/html/?{0}.html'.format(item['id']),
            'source': item['fwjg'],
            'date': time.strftime("%Y-%m-%d", time.localtime(int(item['fbdate'])/1000)),
        }
        return result

