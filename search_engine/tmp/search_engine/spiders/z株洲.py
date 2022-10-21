import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class Z株洲(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '株洲'
    api = "http://searching.hunan.gov.cn/hunan/973000000/news?q={keyword}&searchfields=&sm=0&columnCN=&iszq=&aggr_iszq=&p={page}&timetype=timeqb"
    method = "GET"
    start_page = 0

    def edit_page(self, response):
        total_items_num = response.css("div.time-limit.result").re(
            "相关结果约(.*)个")[0]
        total_page_num = int(total_items_num) // 10 + 1
        return total_page_num

    def edit_items_box(self, response):
        items_box = response.css("div#hits")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("li")
        return items

    def edit_item(self, item):
        data = {
            'url': item.css('div.title > a::attr(href)').get(),
            'title': item.css('div.title > a::attr(title)').getall(),
            'date': item.css('span.source-time::text').get(),
            'type': item.css('div.com-title>span::text').get(),
            'source': item.css('span.source-name::text').get()
        }
        return data
