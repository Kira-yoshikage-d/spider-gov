from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class TangshanSpider(ZhengFuBaseSpider):
    name = '唐山'
    api = 'http://www.tangshan.gov.cn/search.jspx?q={keyword}&channelId=&siteId=1%2C123&tagId=0&date=0&sort=0&startDate=&endDate=&pageNo={page}'
    method = 'GET'

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        text = response.css("div.main_body + div::text").get()
        page = text.split("页")[0].split("/")[1]
        return int(page)


    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        return response.css("div.searchList div")


    def edit_items(self, items_box: Selector) -> Selector:
        """
        将目录索引整理为标准迭代器.
        """
        return items_box

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            "url": item.css("a::attr(href)").get(),
            "title": item.css("a::attr(title)").get(),
            "date": item.css("span::text").get(),
            "type": item.css("a::text").get().split("]")[0].split("[")[1]
        }

        return data
