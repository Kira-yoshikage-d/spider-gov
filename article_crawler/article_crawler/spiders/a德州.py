from article_crawler.baseSpider import baseSpider


class A德州Spider(baseSpider):
    name = '德州'

    @baseSpider.parser('德州', 'dzbee.dezhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div#con_con  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('德州', 'dzbee.dezhou.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('德州', 'dzbee.dezhou.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.warttext  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('德州', 'dzbee.dezhou.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("body > div > div.block.block900 > div:nth-child(3) > div:nth-child(3)  :not(script):not(style)::text").getall()
        }


