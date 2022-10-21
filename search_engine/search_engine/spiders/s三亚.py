from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector

class S三亚Spider(ZhengFuBaseSpider):
    name = "三亚"
    method = "GET"
    debug = True

    api = "http://search.sanya.gov.cn/s?searchWord={keyword}&column=%25E5%2585%25A8%25E7%25AB%2599&pageSize=10&pageNum={page}&siteCode=4602000035&sonSiteCode=&checkHandle=1&searchSource=0&govWorkBean=%257B%257D&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&manualWord={keyword}&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=1"

    def edit_page(self, response: Response) -> int:
        pages: str = response.css("p.fl > span::text").get()
        return int(pages)//10+1
    def edit_items_box(self, response: Response)-> Selector:

        return response.css("div.wordGuide.Residence-permit")

    def edit_item(self, item: Selector) -> dict:
        data = {
            'url': item.css("div.bigTit.clearfix > a::attr(href)").get(),
            'title':item.css("div.bigTit.clearfix > a::attr(title)").get(),
            'date':item.css("p.time > span::text").get(),
            'sourse':item.css("p.time>a::attr(href)").get(),
            'type':item.css("div.bigTit.clearfix > a::attr(data)").get()
        }
        return data
