from article_crawler.baseSpider import baseSpider


class A长治Spider(baseSpider):
    name = '长治'

    @baseSpider.parser('长治', 'www.changzhi.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('长治', 'www.changzhi.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.article-body  :not(script):not(style)::text").getall()
        }
