from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A天津Spider(ZhengFuBaseSpider):
    name: str = '天津'
    debug: bool = False
    api = 'https://www.tj.gov.cn/igs/front/search.jhtml?code=78778b9ded5140d4984030cf8f469303&pageNumber={page}&pageSize=10&searchWord={keyword}&siteId=34&sortByFocus=true&type=2404'
    method = 'GET'

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        total_pages = response.json()["page"]["totalPages"]
        return int(total_pages)

    def edit_items_box(self, response: Response):
        """
        返回目录索引.
        返回 Selector
        """
        return response.json()["page"]["content"]

    def edit_item(self, item: dict) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            "url": item["url"],
            "title": Selector(text=item["title"]).css("  ::text").getall(),
            "date": item["trs_time"],
            "type": item["trs_type"],
            "source": item.get("dept", "无"),
        }
        return data
