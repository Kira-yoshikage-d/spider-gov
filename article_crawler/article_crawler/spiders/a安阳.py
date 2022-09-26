from article_crawler.baseSpider import baseSpider


class A安阳Spider(baseSpider):
    name = '安阳'

    @baseSpider.parser('安阳', 'www.anyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.conBox  ::text").getall()
        }
