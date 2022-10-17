from article_crawler.baseSpider import baseSpider


class A日照Spider(baseSpider):
    name = '日照'

    @baseSpider.parser('日照', 'www.rizhao.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#a  :not(script):not(style)::text").getall()
        }
