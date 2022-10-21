from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector

class s三门峡Spider(ZhengFuBaseSpider):
    name = '三门峡'
    api = "https://smx.gov.cn/pageView/classifiedSearch.html?pageNum={page}&searchText={keyword}&s_lmnrlx=-1&s_fbsj_s=&s_fbsj_e=&protocol="
    method = "GET"
    debug = True

    def edit_page(self, response: Response) -> int:
        pages : str = response.css("div.banner.w.clearfix > div.search.clearfix > div.search_left.fl > div.result.clearfix > p>span::text").get()#.re("<span>(.*?)</span>")[0]
        print(pages)
        return int(pages)//10+1

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        return response.css('div.banner.w.clearfix > div.search.clearfix > div.search_left.fl > div.search_ye >div.itemSearch.clearfix')


    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            'url': item.css('p.returnTitle > a::attr(href)').get(),
            'title': item.css(' p.returnTitle > a::text').getall(),
            'date': item.css('p > span.returnTime::text').get(),
            'type': 'unknow',
            'source': 'unknow'
        }
        return data