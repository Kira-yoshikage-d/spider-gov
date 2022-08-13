import re

from search_engine.basepro import ZhengFuBaseSpider


class JinhuaDbSpider(ZhengFuBaseSpider):
    name = 'Jinhua_db'
    allowed_domains = ['jhnews.com.cn']
    start_urls = ['http://https://www.jhnews.com.cn//']
    api = 'https://jhwxgl.jhnews.com.cn/webSearch/search?searchWord={keyword}&pageNum={page}&order=%7b%22docPubTime%22:%22desc%22%7d'
    method = 'GET'

    def edit_page(self, response):
        raw_data = response.json()
        all_page = raw_data['data']['pageCount']
        return int(all_page)

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data['data']['entities']
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item['title'],
            "url" : item['docPubUrl'],
            "pre_content" : item['abstract'],
            "date" : re.search('\d{4}-\d+-\d+', item['docPubTime']).group()
        }
        return meta_info
