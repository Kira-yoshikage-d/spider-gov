import scrapy
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class Y玉溪Spider(ZhengFuBaseSpider):
    name = '玉溪'
    api = "http://www.yuxi.gov.cn/yxgovfront/search_{page}.jspx?q={keyword}&_s_=1&rangeBy=title&orderBy=time&dir=desc"
    method = "GET"
    debug = False

    def edit_page(self, response: Response) -> int:
        total_num = int(response.css("body > div.search-page.common-padding-bottom > div.search-result > div > "
                                 "div.col.col1.search-list > div.search_msg > span:nth-child(2)::text").re("(\d*)条")[0])
        return total_num // 10 + 1

    def edit_items_box(self, response: Response):
        return response.css("dl")

    def edit_item(self, item) ->dict:
        data = {
            'url' : item.css("dt a::attr(href)").get(),
            'title' : item.css("dt > a::text").getall(),
            'source' : item.css("dd.origin >a::text").get(),
            'date' : item.css("dd.origin >span::text").get(),
            'type' : 'unknown'
        }

        return data
