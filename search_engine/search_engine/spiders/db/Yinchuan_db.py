from search_engine.basepro import ZhengFuBaseSpider


class YinchuanDbSpider(ZhengFuBaseSpider):
    name = 'Yinchuan_db'
    allowed_domains = ['ycen.com.cn']
    start_urls = ['http://http://ycrb.ycen.com.cn//']
    api = 'http://www.ycen.com.cn/search/search.jsp'
    method = 'POST'
    data = {
        'searchword': '',
        'pagestr': '1',
        'pagenum': '10',
        'siteid': '301'
    }

    def edit_data(self, data, keyword, page):
        data['searchword'] = keyword
        data['pagestr'] = str(page)
        return data

    def edit_page(self, response):
        raw_data = response.json()
        all_page = raw_data['allpages']
        return int(all_page)
