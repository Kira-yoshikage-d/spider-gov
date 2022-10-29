from search_engine.basepro import ZhengFuBaseSpider


class ChaoyangDbSpider(ZhengFuBaseSpider):
    name = 'Chaoyang_db'
    allowed_domains = ['cynews.com.cn']
    start_urls = ['http://http://paper.cynews.com.cn//']
    api = 'http://www.cynews.com.cn/search.aspx?key-{keyword},m-0,p-{page}'
    method = 'GET'

    def edit_page(self, response):
        all_page = response.css('div.fenye tr > td > a:last-child::attr(href)').re('p-(\d+)')[0]
        return int(all_page)

    def edit_items_box(self, response):
        items_box = response.css('ul.fbt-list > li')
        return items_box

    def edit_item(self, item):
        #这个网站没有文章预浏览
        meta_info={
            "title": item.css('div.fbt-p > a::attr(title)').get(),
            "url": item.css('div.fbt-p > a::attr(href)').get(),
            "date": item.css('div.fbt-st::text').get()
        }
        return meta_info
