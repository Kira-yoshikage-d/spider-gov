import scrapy
from Hue.basepro import ZhengFuBaseSpider


class XuanchengSpider(ZhengFuBaseSpider):
    name = 'Xuancheng'
    allowed_domains = ['xuancheng.gov.cn']
    start_urls = ['http://http://www.xuancheng.gov.cn//']
    api = "http://search.xuancheng.gov.cn/searchData?keyword={keyword}&siteId=1&field=all&page={page}"
    method = "GET"

    def edit_items_box(self, response):
        items_box = response.css("div.result-list")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("ul li")
        return items

    def edit_item(self, item):
        data = {}
        data['title'] = item.css("h1 > a::text").get()
        data['date'] = item.css("p.p-tips")[0].css("span:nth-child(2)::text").get()
        data['url'] = item.css("p.p-tips")[1].css("span::text").get()
        return data

    def edit_page(self, response):
        total_items_num = response.css("span.fontRed:nth-child(1)::text").get()
        total_page_num = int(total_items_num) // 15 + 1
        return total_page_num
