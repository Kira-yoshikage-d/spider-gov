from search_engine.basepro import ZhengFuBaseSpider


class JianDbSpider(ZhengFuBaseSpider):
    name = 'Jian_db'
    allowed_domains = ['http://www.jgsdaily.com/']
    start_urls = ['http://http://www.jgsdaily.com//']
    api = 'http://app.jgsdaily.com/?app=search&controller=index&action=search&wd={keyword}&mode=full&order=rel&page={page}'
    method = 'GET'

    def edit_page(self, response):
        item_num = response.css('div.column.info::text').re('约(\d+)篇')[0]
        if int(item_num) % 10 == 0:
            all_page = int(item_num) // 10
        else:
            all_page = int(item_num) // 10 + 1
        return min(all_page, 100)

    def edit_items_box(self, response):
        items_box = response.css('div.column.search-result-list > ul > li')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : "".join(item.css('h3 > a *::text').getall()).strip(),
            "url" : item.css('h3 > a::attr(href)').get(),
            "pre_content" : item.css('div > div > p::text').get(),
            "date" : item.css('div > div > span::text').re_first('\d{4}-\d+-\d+')
        }
        return meta_info
