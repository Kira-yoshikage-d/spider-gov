from article_crawler.baseSpider import baseSpider


class a新乡Spider(baseSpider):
    name = '新乡'

    @baseSpider.parser('新乡', 'http://www.xinxiang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#doZoom  :not(script):not(style)::text').getall(),
        }
