from article_crawler.baseSpider import baseSpider


class A三门峡Spider(baseSpider):
    name = '三门峡'

    @baseSpider.parser('三门峡', 'jtysj.smx.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.articleContent  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('三门峡', 'jtysj.smx.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.articleDetails  :not(script):not(style)::text").getall()
        }
