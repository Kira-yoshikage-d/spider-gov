from search_engine.basepro import ZhengFuBaseSpider


class HuaibeiDbSpider(ZhengFuBaseSpider):
    name = 'Huaibei_db'
    allowed_domains = ['hbnews.net']
    start_urls = ['http://http://epaper.hbnews.net/epaper/hbrb/pc/layout//']
    api = 'http://so.hbnews.net/servlet/SearchServlet.do?contentKey={keyword}&titleKey=&authorKey=&nodeNameResult=&subNodeResult=&dateFrom=&dateEnd=&sort=date&op=single&siteID=&changeChannel=&pageNo={page}'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div#result_list > table > tr > td::text').re('\d+')[0]
        if int(item_num) % 20 == 0:
            all_page = int(item_num) // 20
        else:
            all_page = int(item_num) // 20 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('tr.TableBody1')
        return items_box

    def edit_item(self, item):
        #没有发文日期
        meta_info = {
            'title' : item.css('td > a::text').get(),
            'url' : item.css('td > a::attr(href)').get(),
            'pre_content' : "".join(item.css('td *::text').getall()[2:-4]).strip()
        }
        return meta_info

