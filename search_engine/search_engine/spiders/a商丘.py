from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A商丘Spider(ZhengFuBaseSpider):
    name: str = '商丘'
    api = 'https://www.shangqiu.gov.cn/sy?wd={keyword}&tt=0&bt=&et=&kp=0&st=1&siid=1&sid=0&p={page}&vc='
    method = 'GET'
    debug = False
    cookie: str = "__RequestVerificationToken=a2Jl4EdQsmukCAhr3vaFbf_iZTcEJ1VKg48_jFWiwBMFVX1HnifBC_We6LB-qCeiFu3DRg2; ASP.NET_SessionId=nra1jawbzocpyxathorgimse"

    custom_settings: Optional[dict] = {
        'DOWNLOAD_DELAY': 2,
    }

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        total = response.css("div.result-info::text").get().split("到")[1].split("条")[0]
        return int(total)//10+1


    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        return response.css("div.s-result > div.result-list.article.result-list.information.clearfix ul")

    def edit_items(self, items_box: Selector) -> Selector:
        """
        将目录索引整理为标准迭代器.
        """
        return items_box.css("li")

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            "url": item.css("h4 a::attr(href)").get(),
            "title": item.css("h4 a::text").get(),
            "date": item.css("div.attribution::text").get(),
            "source": item.css("div.attribution span::text").get()
        }
        return data
