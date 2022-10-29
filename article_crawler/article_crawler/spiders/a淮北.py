from article_crawler.baseSpider import baseSpider


class A淮北Spider(baseSpider):
    name = '淮北'

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#zoom  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("#J_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.wzcon  :not(script):not(style)::text").getall()
        }
