from search_engine.basepro import ZhengFuBaseSpider


class ShenyangDbSpider(ZhengFuBaseSpider):
    name = 'Shenyang_db'
    allowed_domains = ['cnepaper.com']
    start_urls = ['http://https://m.zazhi.com/article2020/']
    #和乌海那个内蒙古日报一样的差不多一样的api
    api = 'http://fullsearch.cnepaper.com/FullSearch.aspx?__VIEWSTATE=%2FwEPDwULLTE4NTgxMDgzMjQPZBYCAgEPZBYCAgMPDxYCHgtSZWNvcmRjb3VudALIEWRkZInLndMlLBxOIyUYCMnvcaM8UYW6&__VIEWSTATEGENERATOR=4F4D99FC&__EVENTTARGET=&__EVENTARGUMENT=&__EVENTVALIDATION=%2FwEWBQK7hIijAwKMwc%2FlAQK2hea3DQL4p5WKCgLY0YCrAe5%2FvkS26xrsjtjV30A9cWJmQIFm&search_text={keyword}&Txt_SiteStart=2019-11-14&Txt_SiteEnd=&AspNetPager1_input={page}&lblPaperID=4183'
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
