from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider

class LiuzhouSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = 'Liuzhou'
    method = "GET"
    api = "http://www.liuzhou.gov.cn/search/search?page={page}&channelid=222295&searchword={keyword}&keyword={" \
          "keyword}&was_custom_expr=%28{keyword}%28&perpage=10&outlinepage=10&searchscope=&timescope=&timescopecolumn" \
          "=&orderby=-DOCRELTIME&dates=&datee="

    def edit_page(self, response: Response) -> int:
        total = response.css("#search-tools > div.posb > div:nth-child(2) > span:nth-child(1)::text").get()
        return int(total) // 10 + 1

    def edit_items_box(self, response: Response):
        return response.css("body > div.wrapper > div.piece.whole.clearfix > div.content_left.fl.posr > div.total > div:nth-child(3) > table")

    def edit_item(self, item):
        data = {}
        data['url'] = item.css("span.js_zi2 > a::attr(href)").get()
        return data