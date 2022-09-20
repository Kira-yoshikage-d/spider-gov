from article_crawler.baseSpider import baseSpider


class A张家口Spider(baseSpider):
    name = '张家口'

    @baseSpider.parser('张家口', 'www.zjk.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#content  ::text").getall()
        }
