from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class JiyuanSpider(ZhengFuBaseSpider):
    name = '济源'
    api = 'http://sousuo.www.jiyuan.gov.cn/igs/front/search.jhtml?code=971c944454cd42b8b0070c74dbb8cbac&pageNumber={page}&pageSize=10&queryAll=true&searchWord={keyword}&siteId=9'
    method = 'GET'

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        response_dict = response.json()
        return int(response_dict['page']['totalPages'])

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        response_dict = response.json()
        return response_dict['page']['content']

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            'title': item['title'],
            'date': item['trs_time'],
            'source': item['trs_site'],
            'type': item['trs_type'],
            'url': item['url'],
        }
        return data
