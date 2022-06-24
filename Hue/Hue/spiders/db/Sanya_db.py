from Hue.basepro import ZhengFuBaseSpider


class SanyaDbSpider(ZhengFuBaseSpider):
    name = 'Sanya_db'
    allowed_domains = ['sanyarb.com.cn']
    start_urls = ['http://http://epaper.sanyarb.com.cn//']
    api = 'http://stat.sanyarb.com.cn:8098/servlet/SearchServlet.do?contentKey={keyword}&titleKey=&authorKey=&nodeNameResult=&subNodeResult=&dateFrom=&dateEnd=&sort=date&op=single&siteID=&pageNo={page}'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div.content > form > table > tr > td > table > tr > td:last-child::text').re('\s(\d+)\s')[0]
        if int(item_num) % 20 == 0:
            all_page = int(item_num) // 20
        else:
            all_page = int(item_num) // 20 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div.con006.fw')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item.css('h1 > a::text').re_first('(.+?\s)-'),
            "url" : item.css('h1 > a::attr(href)').get(),
            "pre_content" : "".join(item.css('p *::text').getall()).strip(),
            "date" : item.css('h1 > a::text').re_first('\d{4}-\d+-\d+')
        }
        return meta_info
