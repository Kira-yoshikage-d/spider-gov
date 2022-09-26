from article_crawler.baseSpider import baseSpider


class A洛阳Spider(baseSpider):
    name = '洛阳'

    @baseSpider.parser('洛阳', 'www.ly.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("li.wzxqnr  ::text").getall()
        }

    @baseSpider.parser('洛阳', 'www.ly.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.pages_content  ::text").getall()
        }
