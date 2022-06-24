from Hue.basepro import ZhengFuBaseSpider


class ZhongshanDbSpider(ZhengFuBaseSpider):
    name = 'Zhongshan_db'
    allowed_domains = ['zsnews.cn']
    start_urls = ['http://http://www.zsnews.cn/epaper//']
    api = 'http://epaper.zsnews.cn/search/index?keywords={keyword}&type=1&p={page}'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div.num::text').re('约(\d+)个')[0]
        if int(item_num) % 20 == 0:
            all_page = int(item_num) // 20
        else:
            all_page = int(item_num) // 20 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div.left > div')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item.css('div:nth-child(1) > a::text').get(),
            "url" : "http://epaper.zsnews.cn" + item.css('div:nth-child(1) > a::attr(href)').get(),
            "pre_content" : item.css('div:nth-child(2)::text').get(),
            "date" : item.css('div:nth-child(3)::text').re_first('\d{4}-\d+-\d+')
        }
        return meta_info
