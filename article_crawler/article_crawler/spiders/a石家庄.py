from article_crawler.baseSpider import baseSpider



class A石家庄Spider(baseSpider):
    name = '石家庄'

    @baseSpider.parser('石家庄', 'www.sjz.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#conN>div  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('石家庄', 'www.sjz.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('#conN  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('石家庄', 'www.sjz.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css(' div.Section0  :not(script):not(style)::text').getall()
        }
