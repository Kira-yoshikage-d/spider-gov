from article_crawler.baseSpider import baseSpider


class A廊坊Spider(baseSpider):
    name = '廊坊'

    @baseSpider.parser('廊坊', 'http://www.lf.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            "content": response.css("#fontzoom p::text").getall()
        }
