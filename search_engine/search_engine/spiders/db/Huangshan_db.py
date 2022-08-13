from search_engine.basepro import ZhengFuBaseSpider


class HuangshanDbSpider(ZhengFuBaseSpider):
    name = 'Huangshan_db'
    allowed_domains = ['cnepaper.com']
    start_urls = ['http://http://www.hsdaily.cn/index/index.htm/']
    #和沈阳、内蒙古的党报搜索api一样，但是这个有点垃圾，响应有点慢
    api = 'http://fullsearch.cnepaper.com/eso/hsrb.aspx?__VIEWSTATE=%2FwEPDwULLTE4NTgxMDgzMjQPZBYCAgEPZBYCAgMPDxYEHgtSZWNvcmRjb3VudALeAh4QQ3VycmVudFBhZ2VJbmRleAIEZGRk3LTFrIl1RDftNEzTaC7bVOzMzkE%3D&__VIEWSTATEGENERATOR=E0580BCF&__EVENTTARGET=AspNetPager1&__EVENTARGUMENT={page}&__EVENTVALIDATION=%2FwEWBQK%2BzKL6DwKMwc%2FlAQK2hea3DQL4p5WKCgLY0YCrAfZWCbNn2%2BDfWgWWekzJBbGagWh4&search_text={keyword}&Txt_SiteStart=1998-11-14&Txt_SiteEnd=&lblPaperID=1269'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div#content > div.aside > div.aright > b:last-child::text').get()
        if int(item_num) % 10 == 0:
            all_page = int(item_num) // 10
        else:
            all_page = int(item_num) // 10 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div#content > ol#need > li')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title": item.css('span > a::text').re('\s+(\S+)')[0],
            "url": item.css('span > a::attr(href)').get(),
            "pre_content": "".join(item.css('p:nth-child(2) *::text').getall()).strip(),
            "date": item.css('p:last-child::text').re('\d{4}-\d{2}-\d{2}')[0]
        }
        return meta_info
