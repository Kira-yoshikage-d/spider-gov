from Hue.basepro import ZhengFuBaseSpider


class WuhaiDangbaoSpider(ZhengFuBaseSpider):
    name = 'Wuhai_dangbao'
    allowed_domains = ['cnepaper.com']
    start_urls = ['http://http://szb.northnews.cn/nmgrb//']
    #这个api需要指定起止时间，来搜索某个时间段内的文章，参数为Txt_SiteStart=&Txt_SiteEnd=
    api = 'http://fullsearch.cnepaper.com/FullSearch.aspx?__VIEWSTATE=%2FwEPDwULLTE4NTgxMDgzMjQPZBYCAgEPZBYCAgMPDxYEHgtSZWNvcmRjb3VudAI6HhBDdXJyZW50UGFnZUluZGV4AgJkZGRK%2BhLY9iTwGERGt2zdYurdTpwz%2BQ%3D%3D&__VIEWSTATEGENERATOR=4F4D99FC&__EVENTTARGET=AspNetPager1&__EVENTARGUMENT={page}&__EVENTVALIDATION=%2FwEWBQLf%2F%2BruCAKMwc%2FlAQK2hea3DQL4p5WKCgLY0YCrAZWplT95EqkuxqJEtS7Tev4YU%2BFP&search_text={keyword}&Txt_SiteStart=2020-07-01&Txt_SiteEnd=&lblPaperID=1093'
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
