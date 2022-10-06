from article_crawler.baseSpider import baseSpider


class A承德(baseSpider):
    name = '承德'

    @baseSpider.parser('Chengde', 'www.chengde.gov.cn')
    def parser_1(self, response, **kwargs):
        result = {
            'content': response.css("div.cont  :not(script):not(style)::text").getall(),
        }
        return result

    @baseSpider.parser('Chengde', 'www.chengde.gov.cn')
    def parser_2(self, response, **kwargs):
        result = {
            'content': response.css("div.article  :not(script):not(style)::text").getall(),
        }
        return result
