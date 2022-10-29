from article_crawler.baseSpider import baseSpider


class A邢台Spider(baseSpider):
    name = '邢台'

    @baseSpider.parser('邢台', 'www.xingtai.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#zoom  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('邢台', 'www.xingtai.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  :not(script):not(style)::text").getall()
        }

