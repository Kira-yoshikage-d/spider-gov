from article_crawler.baseSpider import baseSpider


class A晋中Spider(baseSpider):
    name = '晋中'

    @baseSpider.parser('晋中', 'www.sxjz.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.conTxt  ::text").getall()
        }
