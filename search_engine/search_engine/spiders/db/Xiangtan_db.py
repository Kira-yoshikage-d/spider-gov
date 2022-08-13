from search_engine.basepro import ZhengFuBaseSpider


class XiangtanDbSpider(ZhengFuBaseSpider):
    name = 'Xiangtan_db'
    allowed_domains = ['xtol.cn']
    start_urls = ['http://http://www.xtol.cn//']
    api = 'https://app.xtol.cn/?app=search&controller=index&action=search&wd={keyword}&type=article&title=1&catid=&order=time&page={page}'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div.search-time > p.f-l > span::text').get()
        if int(item_num) % 10 == 0:
            all_page = int(item_num) // 10
        else:
            all_page = int(item_num) // 10 + 1
        return all_page

    def edit_items_box(self, response):
        items_box = response.css('section.column > section.column-main > dl.search-list > dd')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title": item.css('div.article.title > a::text').get(),
            "url": item.css('div.article.title > a::attr(href)').get(),
            "pre_content": "".join(item.css('div.description > div.texts > p.summary *::text').getall()).strip(),
            "date": item.css('p.result > var::text').re_first('\d{4}-\d+-\d+')
        }
        return meta_info
