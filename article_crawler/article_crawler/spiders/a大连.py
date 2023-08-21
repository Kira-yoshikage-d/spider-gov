from article_crawler.baseSpider import baseSpider


class a大连Spider(baseSpider):
    name = '大连'

    @baseSpider.parser('大连', 'www.dl.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  ::text').getall(),
        }
    @baseSpider.parser('大连', 'www.dl.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.article-content  ::text').getall(),
        }

    @baseSpider.parser('大连', 'www.dl.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('div.art_con  ::text').getall(),
        }
    @baseSpider.parser('大连', 'www.dl.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css('div.article-body  ::text').getall(),
        }
    @baseSpider.parser('大连', 'www.dl.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css('#zoom>div.d1  ::text').getall(),
        }