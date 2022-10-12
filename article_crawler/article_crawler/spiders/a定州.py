from article_crawler.baseSpider import baseSpider


class A定州Spider(baseSpider):
    name = '定州'

    @baseSpider.parser('定州', 'www.dzs.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#conN  :not(script):not(style)::text").getall()
        }
