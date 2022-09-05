from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class ZhengzhouSpider(ZhengFuBaseSpider):
    name = 'zhengzhou'
    api = 'http://www.zhengzhou.gov.cn/search_{page}.jspx?q={keyword}&result_type=2&source=&place=&cid=&mid=&orderby=1'
    method = 'GET'

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        page = response.css("#full_text_search_form div.page-tile a:nth-last-child(3)::text").get()
        return int(page)

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        return response.css("div.full_text_search_common-list.full_text_search_page-list > a")

    def edit_item(self, item: Response) -> dict:
        """
        从迭代器中提取item.
        """
        result = {
            'url': item.css("::attr(href)").get(),
            'title': item.css("span::text").get(),
            'date': item.css("em:nth-child(2)::text").get(),
            'source': item.css("em:nth-child(3)::text").get(),
        }

        return result
