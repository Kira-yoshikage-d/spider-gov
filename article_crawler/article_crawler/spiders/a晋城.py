from article_crawler.baseSpider import baseSpider


class A晋城Spider(baseSpider):
    name = '晋城'

    @baseSpider.parser('晋城', 'www.jcgov.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.generalContent  ::text").getall()
        }
