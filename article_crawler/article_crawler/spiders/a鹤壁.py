from article_crawler.baseSpider import baseSpider


class A鹤壁Spider(baseSpider):
    name = '鹤壁'

    @baseSpider.parser('鹤壁', 'www.hebi.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.zoom  :not(script):not(style)::text").getall()
        }
