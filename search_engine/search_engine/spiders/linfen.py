from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
from search_engine import g_keywords


class LinfenSpider(ZhengFuBaseSpider):
    debug = False 
    name = '临汾'
    api = 'http://www.linfen.gov.cn/irs/front/search'
    method = "POST"
    headers = ZhengFuBaseSpider.headers
    headers['Content-Type'] = 'application/json'
    data = {
        "code": "181936c3700",
        "configCode": "",
        "codes": "",
        "searchWord": "{keyword}",
        "historySearchWords": [],
        "dataTypeId": "1823",
        "orderBy": "related",
        "searchBy": "all",
        "appendixType": "",
        "granularity": "ALL",
        "beginDateTime": "",
        "endDateTime": "",
        "isSearchForced": 0,
        "filters": [],
        "pageNo": "{page}",
        "pageSize": 10
    }

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        data = response.json()
        totla_page = data['data']['pager']['pageSize']
        return int(totla_page)

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        data = response.json()
        return data['data']['middle']['list']

    def edit_item(self, item: dict) -> dict:
        """
        从迭代器中提取item.
        """
        result: dict[str, str] = {
            'title': item['title'],
            'url': item['url'],
            'date': item['time'],
            'source': item['source'],
        }
        return result

