from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider

class S三亚(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '三亚'
    method = "GET"
    api = "http://search.sanya.gov.cn/s?searchWord={keyword}&column=%E5%85%A8%E7%AB%99&pageSize=10&pageNum={page}" \
          "&siteCode=4602000035&sonSiteCode=&checkHandle=1&searchSource=0&govWorkBean=%7B%7D&areaSearchFlag=-1" \
          "&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex" \
          "=&manualWord={keyword}&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=1 "

    def edit_page(self, response: Response) -> int:
        total_num = response.css("body > div:nth-child(3) > div > div.leftSide-layer.fl > div.results-list.clearfix > "
                                 "div > p > span::text").get()
        return int(total_num) // 10 + 1

    def edit_items_box(self, response: Response):
        return response.css("div.wordGuide.Residence-permit")

    def edit_item(self, item):
        data = {
            'url': item.css("div.bigTit.clearfix > a::attr(href)").get(),
            'title':item.css("div.bigTit.clearfix > a::attr(title)").get(),
            'date':item.css("p.time > span::text").get(),
            'sourse':item.css("p.time > a::text").get(),
            'type':item.css("div.bigTit.clearfix > a::attr(data)").get()
        }
        return data

