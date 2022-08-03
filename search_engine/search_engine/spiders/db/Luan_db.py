import re

from Hue.basepro import ZhengFuBaseSpider


class LuanDbSpider(ZhengFuBaseSpider):
    name = 'Luan_db'
    allowed_domains = ['luaninfo.com']
    start_urls = ['http://http://www.luaninfo.com//']
    api = 'https://ht.luaninfo.com/s?wd={keyword}&siid=2&st=0&tt=0&bt=&et=&sid=0&p={page}'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div.s-result > div.result-info::text').re('找到\s(\d+)\s条')[0]
        if int(item_num) % 10 == 0:
            all_page = int(item_num) // 10
        else:
            all_page = int(item_num) // 10 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div.s-result > div:nth-child(2) > ul > li')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : "".join(item.css('h4 > a *::text').getall()).strip(),
            "url" : item.css('h4 > a::attr(href)').get(),
            "pre_content" : "".join(item.css('p *::text').getall()).strip(),
            "date" : re.search('\d{4}/\d+/\d+', item.css('div.attribution::text').get()).group()
        }
        return meta_info
