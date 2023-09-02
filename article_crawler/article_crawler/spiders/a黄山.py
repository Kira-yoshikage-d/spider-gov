from article_crawler.baseSpider import baseSpider


class A黄山Spider(baseSpider):
    name = '黄山'

    @baseSpider.parser('黄山', 'www.huangshan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.wzcon.j-fontContent  ::text').getall()
        }

    @baseSpider.parser('黄山', 'www.ah.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.wzcon.j-fontContent  ::text').getall()
        }

