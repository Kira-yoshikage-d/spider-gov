import re

from Hue.basepro import ZhengFuBaseSpider


class LiuzhouDbSpider(ZhengFuBaseSpider):
    name = 'Liuzhou_db'
    allowed_domains = ['http://www.gxlznews.com/']
    start_urls = ['http://http://www.gxlznews.com//']
    api = 'http://szbs.lznews.gov.cn/servlet/SearchServlet.do?contentKey={keyword}&titleKey=&authorKey=&nodeNameResult=&subNodeResult=&dateFrom=20000705&dateEnd=20300101&sort=date&op=adv&siteID=&pageNo={page}'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('td.white').re('\s(\d+)\s')[0]
        if int(item_num) % 20 == 0:
            all_page = int(item_num) // 20
        else:
            all_page = int(item_num) // 20 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div.con006')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : re.sub('\s-.*', '', item.css('h1 > a::text').get()),
            "url" : item.css('h1 > a::attr(href)').get(),
            "pre_content" : "".join(item.css('p *::text').getall()).strip(),
            "date" : item.css('h1 > a::text').re_first('\d{4}-\d+-\d+')
        }
        return meta_info
