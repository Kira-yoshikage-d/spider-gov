import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class A朝阳Spider(ZhengFuBaseSpider):
    """TODO SCRAPY"""
    name = '朝阳'
    allowed_domains = ['chaoyang.gov.cn']
    start_urls = ['http://chaoyang.gov.cn/']

    start_page = 0
    method = "POST"
    api = "http://www.chaoyang.gov.cn/search/search.ct"
    data = {
        'siteCode': 'CYSZF',
        'isAll': '0',
        'offset': '{page}',
        'limit': '15',
        'template': 'CYSZF',
        'resultOrderBy': '0',
        'ssfw': '2',
        'sswjlx': '1',
        'timefw': '1',
        'columnTypeId': '',
        'searchKey': '{keyword}',
    }

    def edit_items_box(self, response):
        return response.css(".result-li")

    def edit_item(self, item):
        result = {}
        result['url'] = item.css("a.tit::attr(href)").get()
        return result

    def edit_page(self, response):
        try:
            return int(
                response.css(
                    "body > div.sousuo-wrap > div.ss-wrap.wrap-clear > div.left > div.fenye-wrap > span.nowpage::text"
                ).re(".*/(\d+)页")[0])
        except Exception:
            return 0
