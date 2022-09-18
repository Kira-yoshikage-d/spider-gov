from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class CangzhouSpider(ZhengFuBaseSpider):
    name: str = '沧州'
    api: str = 'http://www.cangzhou.gov.cn/guestweb4/s?searchWord={keyword}&column=%E5%85%A8%E9%83%A8&wordPlace=1&orderBy=0&startTime=&endTime=&pageSize=10&pageNum={page}&timeStamp=0&siteCode=1309000040&sonSiteCode=&checkHandle=1&strFileType=&govWorkBean=%7B%7D&sonSiteCode=&areaSearchFlag=-1&secondSearchWords=&topical=&pubName=&countKey=0&uc=0&left_right_index=0'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False
    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Referer": "http://www.cangzhou.gov.cn/",
    }


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("body > div.mainCon.clearfix > div.leftSide-layer.fl > div.results-list.clearfix > p > span::text").get()
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.wordGuide.Residence-permit")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("div.bigTit > a::text").getall(),
            'url': item.css("div.bigTit > a::attr(href)").get(),
            'type': item.css("div.bigTit > span::text").get(),
            'source': item.css("p.time > a::text").get(),
            'date': item.css("p.time > span::text").get(),
        }
        return result

