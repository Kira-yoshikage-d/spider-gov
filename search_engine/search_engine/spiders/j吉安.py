from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
import random
import time

class JianSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '吉安'
    method = "GET"
    debug = False
    api = "https://www.jian.gov.cn/index.php?c=api&m=essearchlist&inputorder=1&keyword={keyword}&messagetype=&siteid=&size=20&time=all&page={page}"

    def edit_page(self, response: Response) -> int:
        data = response.json()
        return int(data.get('total', 0))//10+1

    def edit_items_box(self, response: Response):
        b = random.randint(1, 10)
        time.sleep(b)
        return response.json().get('data')

    def edit_item(self, item):
        result = {}
        result['url'] = item.get('_source', {}).get('url', '')
        result['date'] = item.get('_source', {}).get('inputtime', '')
        result['title'] = item.get('_source', {}).get('title', '')
        result['type'] = item.get('_source', {}).get('category', '')
        return result