from Hue.basepro import ZhengFuBaseSpider


class SanmingDbSpider(ZhengFuBaseSpider):
    name = 'Sanming_db'
    allowed_domains = ['202.109.226.74']
    start_urls = ['http://http://smrb.smnet.com.cn//']
    api = 'http://202.109.226.74:18099/xy/Search.do'
    method = 'POST'
    data = {
        'q': '',
        'pageNo': '1',
        'pageSize': '20',
        'channel': '1',
        'siteID': '1',
        'sort': 'date',
        'paperID': '3'
    }

    def edit_data(self, data, keyword, page):
        data['pageNo'] = str(page)
        data['q'] = keyword
        return data

    def edit_page(self, response):
        raw_data = response.json()
        item_num = raw_data['foundNum']
        if int(item_num) % 20 == 0:
            all_page = int(item_num) // 20
        else:
            all_page = int(item_num) // 20 + 1
        return all_page

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data['article']
        return items_box

    def edit_item(self, item):
        meta_info={
            "title" : item['title'],
            "url" : item['url'],
            "pre_content" : item['enpcontent'],
            "date" : item['date']
        }
        return meta_info
