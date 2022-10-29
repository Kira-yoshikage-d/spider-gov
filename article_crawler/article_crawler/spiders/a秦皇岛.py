from article_crawler.baseSpider import baseSpider


class A秦皇岛Spider(baseSpider):
    name = '秦皇岛'

    @baseSpider.parser('秦皇岛', 'www.qhd.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#thirdtitle  ::text").getall()
        }
