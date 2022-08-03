from Hue.basepro import ZhengFuBaseSpider


class NanjingDbSpider(ZhengFuBaseSpider):
    name = 'Nanjing_db'
    allowed_domains = ['218.94.82.84']
    start_urls = ['http://http://njrb.njdaily.cn//']
    api = 'http://218.94.82.84:8080/search/adsearch.jsp'
    method = 'POST'
    data = {
        'page': '1',
        'context': ''
    }

    def edit_data(self, data, keyword, page):
        data['page'] = str(page)
        data['context'] = keyword
        return data

    def edit_page(self, response):
        item_num = response.css('table:nth-child(6) > tr > td > b::text').get()
        if int(item_num) % 10 == 0:
            all_page = int(item_num) // 10
        else:
            all_page = int(item_num) // 10 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.xpath('//table[@class="bian1"]/tr')
        items_box = items_box[:10]
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item.css('td > table > tr:first-child > td > a::text').get().replace("\n", ""),
            "url" : item.css('td > table > tr:first-child > td > a::attr(href)').get(),
            "pre_content" : "".join(item.css('td > table > tr:nth-child(2) > td *::text').getall()).strip(),
            "date" : item.css('td > table > tr:last-child > td:last-child > a > font::text').re_first('\d{4}-\d{2}-\d{2}')
        }
        return meta_info
