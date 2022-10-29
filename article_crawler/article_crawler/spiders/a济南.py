from article_crawler.baseSpider import baseSpider


class A济南Spider(baseSpider):
    name = '济南'

    @baseSpider.parser('济南', 'www.gangcheng.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('济南', 'www.gangcheng.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.art_con  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('济南', 'www.gangcheng.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('.zoom  :not(script):not(style)::text').getall()
        }
