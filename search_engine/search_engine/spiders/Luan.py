import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class LuanSpider(ZhengFuBaseSpider):
    """TODO FIXME"""
    name = 'Luan'
    method = "GET"
    api = "https://www.luan.gov.cn/site/search/6789941?platformCode=&isAllSite=true&siteId=&columnId=&columnIds" \
          "=&typeCode=public_content&beginDate=&endDate=&fromCode=&keywords={keyword}&oldKeywords=&subkeywords" \
          "=&filterKeyWords=&excColumns=&datecode=&sort=intelligent&orderType=0&fuzzySearch=true&type=&tableColumnId" \
          "=&indexNum=&fileNum=&flag=false&pageIndex={page}&pageSize=10 "

    def edit_items_box(self, response):
        items_box = response.css("div#search_list")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("ul")
        return items

    def edit_item(self, item):
        data = {}
        data['url'] = item.css("li.search-title > a::attr(href)").get()
        return data

    def edit_page(self, response):
        pages = response.css("div.reslut_type")[0].css("span::text").getall()
        total_items_num = sum([int(p) for p in pages])
        total_page = total_items_num // 10 + 1
        return total_page
