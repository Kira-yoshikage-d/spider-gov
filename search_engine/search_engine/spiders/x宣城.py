import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class XuanchengSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '宣城'
    api = "http://search.xuancheng.gov.cn/searchData?keyword={keyword}&siteId=1&field=all&page={page}"
    method = "GET"

    def edit_items_box(self, response):
        items_box = response.css("div.result-list")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("ul li")
        return items

    # ui-view > div.result-list > ul > li:nth-child(1) > h1 > a
    # ui-view > div.result-list > ul > li:nth-child(1) > p:nth-child(3) > span:nth-child(1)
    def edit_item(self, item):
        data = {}
        data['url'] = item.css("p.p-tips")[1].css("span::text").get()
        data['source'] = item.css("p.p-tips")[0].css("span:nth-child(1)::text").get()
        data['title'] = item.css("h1 a::text").getall()
        data['date'] = item.css("p.p-tips")[0].css("span:nth-child(2)::text").get()
        data['type'] = item.css("span.tag::text").get()
        return data

    def edit_page(self, response):
        total_items_num = response.css("span.fontRed:nth-child(1)::text").get()
        total_page_num = int(total_items_num) // 15 + 1
        return total_page_num
