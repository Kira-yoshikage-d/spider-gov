from Hue.basepro import ZhengFuBaseSpider


class PuerDbSpider(ZhengFuBaseSpider):
    name = 'Puer_db'
    allowed_domains = ['puernews.com']
    start_urls = ['http://http://www.puernews.com/perb//']
    api = 'http://www.puernews.com/search/?&keyword={keyword}&term=2&page={page}'
    method = 'GET'

    def edit_page(self, response):
        all_page = response.css('div.page::text').re('\s(\d+)\s页')[0]
        return int(all_page)

    def edit_items_box(self, response):
        items_box = response.css('div.sslist > ul#listul > li')
        return items_box

    def edit_items(self, items_box):
        box = []
        for i in range(int(len(items_box)/2)):
            box.append(items_box[2*i])
        return box

    def edit_item(self, item):
        #没有预浏览
        meta_info = {
            "title" : item.css('h3 > a > span::text').get(),
            "url" : 'http://www.puernews.com' + item.css('h3 > a::attr(href)').get(),
            "date" : item.css('h3 > a > span > font::text').get()
        }
        return meta_info
