from article_crawler.baseSpider import baseSpider


class A吕梁Spider(baseSpider):
    name = '吕梁'

    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#UCAP-CONTENT  ::text").getall()
        }

    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("#contentText  ::text").getall()
        }


    @baseSpider.parser('吕梁', 'www.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.view.TRS_UEDITOR.trs_paper_default.trs_word  ::text").getall()
        }

