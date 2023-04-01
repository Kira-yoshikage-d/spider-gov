from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector

class A河南省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '四川省生态环境厅'
    api: str = 'http://sthjt.sc.gov.cn/guestweb4/s?searchWord={keyword}&column=%25E5%2585%25A8%25E9%2583%25A8&wordPlace=0&orderBy=0&startTime=&endTime=&pageSize=10&pageNum={page}&timeStamp=0&siteCode=5100000086&siteCodes=&checkHandle=1&strFileType=%25E5%2585%25A8%25E9%2583%25A8%25E6%25A0%25BC%25E5%25BC%258F&sonSiteCode=&areaSearchFlag=1&secondSearchWords=&countKey=%200&left_right_index=0'
    method: str = 'GET'
    data: dict[str, Any] = {}
    start_page: int = 0
    debug: bool = False

    def edit_page(self, response: Selector) -> int:
        total = response.css("div.results-list.clearfix p.fl span::text ").get()

        print(total)
        return int(total)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.wordGuide.Residence-permit")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        result = {
            'title': item.css("div.bigTit.clearfix a::text").getall(),
            'url': item.css("div.bigTit.clearfix a::attr(href)").get(),
            'date': item.css("div.listInfoCon.clearfix p.time span.sourceDateFont::text").get(),
            'source': item.css("div.listInfoCon.clearfix p.time a::text").get(),
            'type':item.css("div.bigTit.clearfix span::text").get()
        }
        return result