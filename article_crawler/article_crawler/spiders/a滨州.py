from article_crawler.baseSpider import baseSpider


class A滨州Spider(baseSpider):
    name = '滨州'

    @baseSpider.parser('滨州', 'www.binzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#neirong  ::text").getall()
        }
