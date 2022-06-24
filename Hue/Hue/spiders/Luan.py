import scrapy
from Hue.basepro import ZhengFuBaseSpider


class LuanSpider(ZhengFuBaseSpider):
    name = 'Luan'
    allowed_domains = ['luan.gov.cn']
    start_urls = ['http://http://www.luan.gov.cn//']
    method = "GET"
    api = "http://www.luan.gov.cn/site/search/6789941?platformCode=&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=public_content&beginDate=&endDate=&fromCode=&keywords={keyword}&oldKeywords=&subkeywords=&filterKeyWords=&excColumns=&datecode=&sort=intelligent&orderType=0&fuzzySearch=true&type=&tableColumnId=&indexNum=&fileNum=&flag=false&pageIndex={page}&pageSize=10"

    def edit_items_box(self, response):
        items_box = response.css("div#search_list")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("ul")
        return items

    def edit_item(self, item):
        data = {}
        data['title'] = item.css("li.search-title > a::attr(title)").get()
        data['url'] = item.css("li.search-title > a::attr(href)").get()
        data['date'] = item.css("li:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)::text").get()
        return data

    def edit_page(self, response):
        pages = response.css("div.reslut_type")[0].css("span::text").getall()
        total_items_num = sum([int(p) for p in pages])
        total_page = total_items_num // 10 + 1
        return total_page
