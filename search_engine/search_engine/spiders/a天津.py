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
        total = response.json().get("page")["total"]
        return int(total)//10 + 1

    def edit_items_box(self, response: Response):
        """
        返回目录索引.
        返回 Selector
        """
        return response.json().get("page")["content"]

    def edit_items(self, items_box):
        """
        将目录索引整理为标准迭代器.
        """
        return items_box

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            "url": item["url"],
            "title": item["title"],
            "date": item["trs_time"].split("T")[0],
            "type": item["trs_type"]
        }

        return data
