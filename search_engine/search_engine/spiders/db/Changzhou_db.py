from search_engine.basepro import ZhengFuBaseSpider


class ChangzhouDbSpider(ZhengFuBaseSpider):
    name = 'Changzhou_db'
    allowed_domains = ['cz001.com.cn']
    start_urls = ['http://http://epaper.cz001.com.cn//']
    api = 'https://esearch.cz001.com.cn/xy/Search.do'
    method = 'POST'
    data = {
        'q': '',
        'pageNo': "1",
        'pageSize': '20',
        'siteID': '1',
        'sort': 'date desc',
        'paperID': '1'
    }

    def edit_data(self, data, keyword, page):
        data['q'] = keyword
        data['pageNo'] = str(page)
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
