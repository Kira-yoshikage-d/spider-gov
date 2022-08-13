import scrapy
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class HefeiSpider(ZhengFuBaseSpider):
    """未知错误"""
    name = 'Hefei'
    start_urls = ['http://http://www.hefei.gov.cn//']
    method = "GET"
    api = "https://www.hefei.gov.cn/site/search/6784331?platformCode=&fuzzySearch=false&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=&endDate=&fromCode=title&keywords={keyword}&oldKeywords=&subkeywords=&filterKeyWords=&excColumns=&dateKey=&datecode=&sort=intelligent&type=&tableColumnId=&indexNum=&fileNum=&flag=false&pageIndex={page}&pageSize=10"

    def edit_items_box(self, response: Response):
        return response.css("#search_list > ul.search-list")

    def edit_item(self, item: scrapy.Selector):
        result = {'url': item.css("li.search-url a::attr(href)").get()}
        return item
