from article_crawler.baseSpider import baseSpider


class A聊城Spider(baseSpider):
    name = '聊城'

    @baseSpider.parser('聊城', 'www.liaocheng.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#Zoom  :not(script):not(style)::text").getall()
        }
