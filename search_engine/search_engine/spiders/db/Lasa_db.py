from Hue.basepro import ZhengFuBaseSpider


class LasaDbSpider(ZhengFuBaseSpider):
    name = 'Lasa_db'
    allowed_domains = ['souxz.cn']
    start_urls = ['http://http://www.lasa-eveningnews.com.cn//']
    api = 'http://www.souxz.cn/search/res/search?tabName=_news&Searchword=%E7%85%A4%E7%82%AD&item_SITEID=0;7&PageIndex=0&pageSize=15&orderby=-docpubtime'
    method = 'GET'
    start_page = 0

    def edit_page(self, response):
        raw_data = response.json()
        item_num = raw_data['page_info']['count']
        if int(item_num) % 15 == 0:
            all_page = int(item_num) // 15
        else:
            all_page = int(item_num) // 15 + 1
        return all_page

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data['datas']
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item['MetaDataTitle'],
            "url" : item['_DOCPUBURL'],
            "pre_content" : item['Content'],
            "date" : item['SysTime']['fullDate']
        }
        return meta_info
