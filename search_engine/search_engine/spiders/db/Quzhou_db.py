from Hue.basepro import ZhengFuBaseSpider


class QuzhouDbSpider(ZhengFuBaseSpider):
    name = 'Quzhou_db'
    allowed_domains = ['http://www.qz828.com/']
    start_urls = ['http://http://www.qz828.com//']
    api = 'http://zhannei.baidu.com/cse/search?q={keyword}&p={page}&s=7028640854484833084&nsid=&entry=1'
    method = 'GET'
    start_page = 0

    def edit_page(self, response):
        item_num = response.css('div#results > span::text').re('\d+')[0]
        if int(item_num) % 10 == 0:
            all_page = int(item_num) // 10
        else:
            all_page = int(item_num) // 10 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div#results > div.result.f.s0')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item.css('h3 > a::text').get(),
            "url" : item.css('h3 > a::attr(href)').get(),
            "pre_content" : "".join(item.css('div > div.c-content > div.c-abstract *::text').getall()).strip(),
            "date" : item.css('div > div.c-content > div:last-child > span::text').re_first('\d{4}-\d+-\d+')
        }
        return meta_info
