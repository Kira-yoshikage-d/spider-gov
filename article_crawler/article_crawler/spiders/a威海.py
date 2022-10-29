from article_crawler.baseSpider import baseSpider


class A威海Spider(baseSpider):
    name = '威海'

    @baseSpider.parser('威海', 'www.weihai.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.art_con  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('威海', 'www.weihai.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.xxgkcont  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('威海', 'www.weihai.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("#content  :not(script):not(style)::text").getall()
        }
