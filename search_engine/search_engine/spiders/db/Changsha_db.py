from Hue.basepro import ZhengFuBaseSpider


class ChangshaDbSpider(ZhengFuBaseSpider):
    name = 'Changsha_db'
    allowed_domains = ['icswb.com']
    start_urls = ['http://https://www.icswb.com//']
    api = 'https://so.icswb.com/default.php?mod=search&m=no&syn=no&f=_all&s=s_show_date_DESC&temp=&p={page}&ps=20&site_id=2&range=&search_target=1&search_key={keyword}&search_column=&search_channel_id=0&search_version=0'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div#res-neck > strong::text').get()
        if int(item_num) % 20 == 0:
            all_page = int(item_num) // 20
        else:
            all_page = int(item_num) // 20 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div.outer > div.res-doc')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item.css('h3 > a::text').get(),
            "url" : item.css('h3 > a::attr(href)').get(),
            "pre_content" : "".join(item.css('p *::text').getall()).strip(),
            "date" : item.css('ul > li::text').get()
        }
        return meta_info
