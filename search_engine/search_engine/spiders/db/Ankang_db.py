from search_engine.basepro import ZhengFuBaseSpider
import re


class AnkangDbSpider(ZhengFuBaseSpider):
    name = 'Ankang_db'
    allowed_domains = ['akxw.cn']
    start_urls = ['http://https://sjk.akxw.cn//']
    api = 'https://sjk.akxw.cn/epaper/search.do?m=list&ajax=true'
    method = 'POST'
    keywords = ['煤炭']
    data = {
        'senior': '1',
        'searchText': '煤炭',
        'keywords': '煤炭',
        'searchType': '0',
        'keywords_ad': '煤炭',
        'pageSize': '10',
        'pageNo': '1'
    }

    def edit_data(self, data, keyword, page):
        data['searchText'] = keyword
        data['keywords'] = keyword
        data['keywords_ad'] = keyword
        data['pageNo'] = str(page)
        return data

    def edit_page(self, response):
        txt = response.text
        item_num = re.search('共(\d+)条', txt).group(1)
        if int(item_num) % 10 == 0:
            all_page = int(item_num) // 10
        else:
            all_page = int(item_num) // 10 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('div.seacher_content > ul > li')
        return items_box

    def edit_item(self, item):
        #没有预浏览信息
        meta_info = {
            "title" : item.css('a::text').get().replace('\t', "").replace('\r',"").replace('\n',""),
            "url" : 'https://sjk.akxw.cn' + item.css('a::attr(onclick)').get().replace("doView('", "").replace("')", ""),
            "date" : item.css('span:last-child').re_first('\d{4}-\d+\d+')
        }
        return meta_info
