from article_crawler.baseSpider import baseSpider


class A柳州Spider(baseSpider):
    name = '柳州'

    @baseSpider.parser('柳州', 'www.liuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom > div:nth-child(1)  ::text').getall()
        }

    @baseSpider.parser('柳州', 'swj.liuzhou.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.contentTextBox ::text').getall()
        }


