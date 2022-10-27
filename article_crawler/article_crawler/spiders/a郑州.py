from article_crawler.baseSpider import baseSpider


class A郑州Spider(baseSpider):
    name = '郑州'

    @baseSpider.parser('郑州', 'amr.zhengzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.news_content_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('郑州', 'amr.zhengzhou.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.news_content_text  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('郑州', 'amr.zhengzhou.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.content-text  :not(script):not(style)::text").getall()
        }
