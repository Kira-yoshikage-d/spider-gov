from Hue.basepro import ZhengFuBaseSpider


class YantaiDbSpider(ZhengFuBaseSpider):
    name = 'Yantai_db'
    allowed_domains = ['shm.com.cn']
    start_urls = ['http://http://www.shm.com.cn/paper//']
    api = 'http://so.shm.com.cn/cse/search?q={keyword}&p={page}&s=9326267908929357622&nsid=2'
    method = 'GET'
    start_page = 0

    def edit_page(self, response):
        item_num = response.css('div#results > span::text').re('结果(\d+)个')[0]
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
            "pre_content" : "".join(item.css('div > div.c-abstract-image > div.c-abstract::text').getall()).strip(),
            "date" : item.css('div:last-child >span::text').re_first('\d{4}-\d+-\d+')
        }
        return meta_info
