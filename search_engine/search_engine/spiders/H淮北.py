from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector

class H淮北Spider(ZhengFuBaseSpider):
    name = '淮北'
    api = "https://www.huaibei.gov.cn/site/tpl/3361?isAllSite=true&platformCode=&siteId=&columnId=&columnIds=&typeCode=&beginDate=&endDate=&fromCode=title&keywords={keyword}&excColumns=&datecode=&sort=intelligent&type=&tableColumnId=&subkeywords=&orderType=0&indexNum=&fileNum=&pid=&language=&flag=false&searchType=&searchTplId=&fuzzySearch=true&internalCall=&catIds=&colloquial=false&pageIndex={page}&pageSize=10"
    method = "GET"
    debug = False

    def edit_page(self, response: Response):
        total1 = response.css("div.searchType-column>ul>li:nth-child(1)>a>span::text").get()
        total2 = response.css("div.searchType-column>ul>li:nth-child(2)>a>span::text").get()
        total3 = response.css("div.searchType-column>ul>li:nth-child(3)>a>span::text").get()
        total4 = response.css("div.searchType-column>ul>li:nth-child(4)>a>span::text").get()
        total = int(total1)+int(total2)+int(total3)+int(total4)
        pages = int(total)//10+1
        print(pages)
        return pages

    def edit_items_box(self, response: Response) -> Selector:
        items_box = response.css("#search_list > ul")
        return items_box

    def edit_item(self, item):
        data = {
            'url':item.css("li.search-title > a::attr(href)").get(),
            'title': item.css("li.search-title > a::attr(title)").get(),
            'type': item.css("li.search-title > span::text").get(),
            'source':item.css("li.search-resources>span:nth-child(2)::text").get(),
            'date':item.css("li.search-resources>span:nth-child(3)::text").get()
        }
        return data

