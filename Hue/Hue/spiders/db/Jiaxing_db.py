import re

from Hue.basepro import ZhengFuBaseSpider


class JiaxingDbSpider(ZhengFuBaseSpider):
    name = 'Jiaxing_db'
    allowed_domains = ['cnjxol.com']
    start_urls = ['http://http://jxrb.cnjxol.com//']
    api = 'https://www.cnjxol.com/jxzx/search/fullTableSearch'
    method = 'POST'
    start_page = 0
    data = {
        'content': '煤炭',
        'pageNum': '0',
        'pageSize': '30',
        'order': '{"date": "desc"}'
    }

    def edit_data(self, data, keyword, page):
        data['content'] = keyword
        data['pageNum'] = str(page)
        return data

    def edit_page(self, response):
        raw_data = response.json()
        all_page = raw_data['totalPage']
        return int(all_page)

    def edit_items_box(self, response):
        items_box = response.json()['results']
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item['title'],
            "url" : item['docpuburl'],
            "pre_content" : re.sub('\s|<.+?>', '', item['content']),
            "date" : re.search('\d{4}-\d+-\d+', item['docpubtime']).group()
        }
        return meta_info
