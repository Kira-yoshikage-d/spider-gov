from article_crawler.baseSpider import baseSpider


class A阳泉Spider(baseSpider):
    name = '阳泉'

    @baseSpider.parser('阳泉', 'www.yq.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.content-body  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('阳泉', 'www.yq.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  :not(script):not(style)::text").getall()
        }
