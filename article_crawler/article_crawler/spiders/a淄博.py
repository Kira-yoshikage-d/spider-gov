from article_crawler.baseSpider import baseSpider


class A淄博Spider(baseSpider):
    name = '淄博'

    @baseSpider.parser('淄博', 'cg.zibo.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#details-content  :not(script):not(style)::text").getall()
        }
