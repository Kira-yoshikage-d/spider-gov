from Hue.basepro import ZhengFuBaseSpider


class XuanchengDbSpider(ZhengFuBaseSpider):
    name = 'Xuancheng_db'
    allowed_domains = ['routeryun.com']
    start_urls = ['http://http://xcrb.yunpaper.cn//']
    api = 'http://search.epaper.routeryun.com/result.php?mediaid=232&rel=xcrb.yunpaper.cn&q={keyword}&page={page}'
    method = 'GET'

    def edit_page(self, response):
        all_page = response.css('div.resultArea > p.resultTotal > span.info > span.totalPage::text').get()
        return int(all_page) + 1

    def edit_items_box(self, response):
        items_box = response.css('div.resultArea > div.resultList > div.resultItem')
        return items_box

    def edit_item(self, item):
        meta_info = {
            "title" : item.css('div.itemHead > a::text').get(),
            "url" : item.css('div.itemHead > a::attr(href)').get(),
            "pre_content" : item.css('div.itemBody::text').get(),
            "date" : item.css('div.itemFoot > span.info > span.value::text').get()
        }
        return meta_info

