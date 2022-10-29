from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response

class LasaSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '拉萨'
    method = "GET"
    api = "http://www.lasa.gov.cn/search4/s?searchWord={keyword}&column=%E6%9C%AC%E7%AB%99&pageSize=10" \
          "&pageNum={page}&siteCode=5401000001&sonSiteCode=&checkHandle=1&searchSource=0&govWorkBean=%7B%7D&areaSearchFlag" \
          "=-1&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex" \
          "=&manualWord=%E7%85%A4%E7%82%AD&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0 "
    start_page = 0
    debug  = False
    def edit_page(self, response: Response) -> int:
        total = response.css("body > div:nth-child(3) > div > div.leftSide-layer.fl > div.results-list.clearfix > div > p > span::text").get()
        return int(total) // 10 + 1

    def edit_items_box(self, response: Response):
        return response.css("div.wordGuide.Residence-permit")

    # \32  > div.listInfoCon.clearfix > div > p.time > span
    def edit_item(self, item):
        result = {}
        result['url'] = item.css("div.bigTit.clearfix > a::attr(href)").get()
        result['title'] = item.css("div.bigTit.clearfix > a::attr(title)").get()
        result['date'] = item.css("div.listInfoCon.clearfix > div.listIntro.fl > p.time > span::text").get()
        result['source'] = item.css("div.listInfoCon.clearfix > div.listIntro.fl > p.time > a::text").get()
        result['type'] = item.css("div.bigTit.clearfix > span::text").get()

        return result
