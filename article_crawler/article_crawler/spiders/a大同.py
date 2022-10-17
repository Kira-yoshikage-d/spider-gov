from article_crawler.baseSpider import baseSpider


class A大同Spider(baseSpider):
    name = '大同'

    @baseSpider.parser('大同', 'www.dt.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  :not(script):not(style)::text").getall()
        }
