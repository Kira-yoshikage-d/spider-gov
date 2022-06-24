from Hue.basepro import ZhengFuBaseSpider


class HefeiDbSpider(ZhengFuBaseSpider):
    name = 'Hefei_db'
    allowed_domains = ['hf365.com']
    start_urls = ['http://http://www.hf365.com//']
    api = "http://app.hf365.com/?app=search&controller=index&action=search&wd={keyword}&mode=full&type=article&order=time&page={page}"
    method = 'GET'

    def edit_page(self, response):
        #这个api会搜索出很多东西，但是最大显示页数只有100页
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
            "title" : item.css('h3.title > a::text').get(),
            "url" : item.css('h3.title > a::attr(href)').get(),
            "pre_content" : item.css("div.m-imagetext > div > p::text").get(),
            "date" : item.css('div.m-imagetext > div > span::text').re_first('\d{4}-\d{2}-\d{2}')
        }
        return meta_info
