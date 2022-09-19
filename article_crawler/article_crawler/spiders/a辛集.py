from article_crawler.baseSpider import baseSpider


class A辛集Spider(baseSpider):
    name = '辛集'

    @baseSpider.parser('辛集', 'www.xinji.gov.cn')
    def parser_1(self, response, **kwargs):
        result = {
            'content': response.css('#UCAP-CONTENT  ::text').getall()
        }
        return result
