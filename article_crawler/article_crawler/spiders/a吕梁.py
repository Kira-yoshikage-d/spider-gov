from article_crawler.baseSpider import baseSpider


class A吕梁Spider(baseSpider):
    name = '吕梁'

    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#UCAP-CONTENT  :not(style):not(script)::text").getall()
        }

    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("#contentText  :not(style):not(script)::text").getall()
        }

    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.view.TRS_UEDITOR.trs_paper_default.trs_word  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  :not(style):not(script)::text").getall()
        }

    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css("div.n  :not(style):not(script)::text").getall()
        }
