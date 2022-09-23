from article_crawler.baseSpider import baseSpider


class A沧州Spider(baseSpider):
    name = '沧州'

    @baseSpider.parser('沧州', 'cgj.cangzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.articlecon  ::text").getall()
        }

    @baseSpider.parser('沧州', 'cgj.cangzhou.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.file_detail  ::text").getall()
        }
