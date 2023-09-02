from article_crawler.baseSpider import baseSpider


class A沧州Spider(baseSpider):
    name = '沧州'

    @baseSpider.parser('沧州', 'cgj.cangzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.articlecon  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('沧州', 'cgj.cangzhou.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.file_detail  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('沧州', 'cgj.cangzhou.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.gk_zn_con  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('沧州', 'cgj.cangzhou.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("div.gk_zn_con  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('沧州', 'www.cangzhou.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css("div.contentmain div.text::text").getall()
        }

    @baseSpider.parser('沧州', 'hb.cangzhou.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css("div.articlecon::text").getall()
        }

    @baseSpider.parser('沧州', 'www.czyh.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css("div.file_detail::text").getall()
        }