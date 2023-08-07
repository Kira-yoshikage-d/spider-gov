from article_crawler.baseSpider import baseSpider

class A̫ԭSpider(baseSpider):
    name = '̫ԭ'

    @baseSpider.parser('̫ԭ', 'www.taiyuan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#Zoom  :not(script):not(style)::text').getall()
        }

    # @baseSpider.parser('̫ԭ', 'www.taiyuan.gov.cn')
    # def parser_2(self, response, **kwargs):
    #     return {
    #         'content': response.css('div.nrcontent  :not(script):not(style)::text').getall()
    #     }

    # @baseSpider.parser('̫ԭ', 'www.taiyuan.gov.cn')
    # def parser_3(self, response, **kwargs):
    #     return {
    #         'content': response.css('div.content  :not(script):not(style)::text').getall()
    #     }

    # @baseSpider.parser('̫ԭ', 'www.taiyuan.gov.cn')
    # def parser_4(self, response, **kwargs):
    #     return {
    #         'content': response.css('div.xl_cont  :not(script):not(style)::text').getall()
    #     }