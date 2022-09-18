from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class ChangzhiSpider(ZhengFuBaseSpider):
    name = '长治'
    api = 'https://www.changzhi.gov.cn/trs-search/trssearch/v2/searchAll.do?siteId=4&searchTag=all&allKeywords={keyword}&fullKeywords=&orKeywords=&notKeywords=&sort=&position=0&organization=&pageNum={page}&pageSize=10&zcYear=&isAlways=1&fileTag='
    method = 'GET'
    debug = False 

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        data = response.json()
        return int(data['data']['total']) // 10 + 1

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        data = response.json()
        return data['data']['data']

    def edit_item(self, item):
        """
        从迭代器中提取item.
        """
        result = {
            'title': item['title'],
            'date': item['docpubtime'],
            'source': item['sitedesc'],
            'url': item['docpuburl'],
            'type': item['chnldesc'],
        }
        return result
