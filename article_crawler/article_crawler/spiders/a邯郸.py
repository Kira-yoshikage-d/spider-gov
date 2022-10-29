from article_crawler.baseSpider import baseSpider


class A邯郸Spider(baseSpider):
    name = '邯郸'

    @baseSpider.parser('邯郸', 'hd.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('邯郸', 'hd.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.zzy_wz.clearfix  :not(script):not(style)::text").getall()
        }



