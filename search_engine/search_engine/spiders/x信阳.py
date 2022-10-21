from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector

class X信阳(ZhengFuBaseSpider):
    name = '信阳'
    api = "https://search1.henan.gov.cn/jrobot/search.do?_cus_lq_field_107=&_cus_eq_field_105=&_cus_eq_field_110=&_cus_pq_content=&_cus_eq_field_118=&_cus_eq_field_119=&_cus_eq_field_108=&_cus_eq_field_111=&_cus_eq_field_113=&_cus_eq_field_112=&webid=450001&pg=12&p={page}&tpl=&category=&_cus_query=&_cus_pq_content=&q={keyword}&pos=&od=&date=&date="
    method = "GET"
    debug: bool = True

    def edit_page(self, response: Response) -> int:
        pages = response.css("#jsearch-info-box::attr(data-total)").get()
        return int (pages)//12+1

    def edit_items_box(self,response: Response) -> Selector:
        return response.css("#jsearch-result-items > div.jsearch-result-box")

    def edit_item(self,item)->dict:
        data = {
            'url':item.css("div.jsearch-title a::attr(href)").get(),
            'date':item.css("div.jsearch-result-abs-content span::text").get(),
            'source':"unknown",
            'type':"unknown",
            'title':item.css("div.jsearch-result-title a::text").getall()
        }
        return data

