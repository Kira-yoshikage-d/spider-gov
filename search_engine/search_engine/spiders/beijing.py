from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class BeijingSpider(ZhengFuBaseSpider):
    # TODO 北京的要重新写
    name = 'beijing'
    api = 'www.beijing.gov.cn'
    method = 'GET'

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        pass

    def edit_data(self, data: dict, keyword: str, page: int, **kwargs) -> dict:
        """
        返回POST数据.
        """
        pass

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        pass

    def edit_items(self, items_box: Selector) -> Selector:
        """
        将目录索引整理为标准迭代器.
        """
        return items_box

    def edit_item(self, item) -> dict:
        """
        从迭代器中提取item.
        """
        return item
