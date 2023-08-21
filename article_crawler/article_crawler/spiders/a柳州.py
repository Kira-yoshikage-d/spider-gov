<<<<<<< HEAD
from article_crawler.baseSpider import baseSpider


class A柳州Spider(baseSpider):
    name = '柳州'

    @baseSpider.parser('柳州', 'www.liuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom > div:nth-child(1)  ::text').getall()
        }

    @baseSpider.parser('柳州', 'swj.liuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.contentTextBox ::text').getall()
        }
=======
from article_crawler.baseSpider import baseSpider


class a柳州Spider(baseSpider):
    name = '柳州'

    @baseSpider.parser('柳州', 'www.liuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.contentTextBox  :not(script):not(style)::text').getall(),
        }
>>>>>>> 20b70eee9a3d24e3594605de61b7683cffe1e7f6
