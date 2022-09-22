from article_crawler.baseSpider import baseSpider


class A天津Spider(baseSpider):
    name = '天津'

    @baseSpider.parser('天津', 'www.tj.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#zoom  ::text").getall()
        }

    @baseSpider.parser('天津', 'www.tj.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("#xlrllt  ::text").getall()
        }

    @baseSpider.parser('天津', 'www.tj.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.common-content  ::text").getall()
        }
