from Hue.basepro import ZhengFuBaseSpider


class ChenzhouDbSpider(ZhengFuBaseSpider):
    name = 'Chenzhou_db'
    allowed_domains = ['czxww.cn']
    start_urls = ['http://http://e.czxww.cn//']
    api = 'http://www.czxww.cn:8088/xy/Search.do'
    #网站有点垃圾，响应不快
    method = 'POST'
    data = {
        'q': '',
        'pageNo': '',
        'pageSize': '20',
        'channel': '1',
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
        meta_info = {}
        meta_info["title"] = item['title']
        if item['title']:
            meta_info["url"] = item['url']
        else:
            meta_info["url"] = item['urlpad']
        meta_info["pre_content"] = item['enpcontent']
        meta_info["date"] = item['date']

        return meta_info

