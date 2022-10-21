from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
class z株洲Spider(ZhengFuBaseSpider):
    name = '株洲'
    method = "GET"
    api = "http://searching.hunan.gov.cn/hunan/973000000/news?q={keyword}&searchfields=&sm=0&columnCN=&iszq=&aggr_iszq=&p={page}&timetype=timeqb"
    debug = False

    def edit_page(self, response: Response) -> int:
        pages :str =response.css("div.time-limit.result>p::text").re("相关结果约(.*?)个")[0]
        return int(pages)//10+1

    def edit_items_box(self, response: Response) -> Selector:
        return response.css("li.active")

    def edit_item(self, item: Selector) -> dict:
        data = {
            'url': item.css('div.title > a::attr(href)').get(),
            'title': item.css('div.title > a::attr(title)').getall(),
            'date': item.css('span.source-time::text').get(),
            'type': item.css('div.com-title>span::text').get(),
            'source': item.css('span.source-name::text').get()
        }
        return data