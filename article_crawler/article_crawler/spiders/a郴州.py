from article_crawler.baseSpider import baseSpider


class A郴州Spider(baseSpider):
    name = '郴州'

    @baseSpider.parser('郴州', 'www.czs.gov.cn')
    def parser_1(self, response, **kwargs):
        result = {
            'content': response.css("div.arc  ::text").getall()
        }
        return result

    @baseSpider.parser('郴州', 'www.czs.gov.cn')
    def parser_2(self, response, **kwargs):
        result = {
            'content': response.css("div.mh-applica  ::text").getall()
        }
        return result

    @baseSpider.parser('郴州', 'www.czs.gov.cn')
    def parser_3(self, response, **kwargs):
        result = {
            'content': response.css("#zoom  ::text").getall()
        }
        return result

