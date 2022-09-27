from article_crawler.baseSpider import baseSpider


class A枣庄Spider(baseSpider):
    name = '枣庄'

    @baseSpider.parser('枣庄', 'www.zaozhuang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.zwnr  ::text").getall()
        }

