from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class HebiSpider(ZhengFuBaseSpider):
    name = '鹤壁'
    api = 'https://www.hebi.gov.cn/api-gateway/jpaas-jsearch-web-server/interface/search/info?websiteid=410600000000&q={keyword}&pg=&cateid=071f5fdb0eeb4262b2b0faf48c0e62d0&serviceId=e3ef28ec652b47ce8f5b65a4f701066e&p={page}'
    method = 'GET'

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        response_dict = response.json()
        total_items = int(response_dict['data']['searchResult']['total'])
        return total_items // 15 + 1

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        response_dict = response.json()
        return response_dict["data"]["searchResult"]["result"]

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        selector = Selector(text=item)
        data = {
            'title': selector.css("div.titleWrapper > a::attr(data-title)").get(),
            'source': selector.css("div.sourceTime span:nth-child(1)::text").get(),
            'date': selector.css("div.sourceTime span:nth-child(2)::text").get(),
            'url': selector.css("div.titleWrapper > a::attr(href)").get(),
        }
        return data
