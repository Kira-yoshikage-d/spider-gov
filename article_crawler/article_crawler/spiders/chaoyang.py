from article_crawler.baseSpider import baseSpider


class ChaoyangSpider(baseSpider):
    name = 'chaoyang'

    @baseSpider.parser('chaoyang', 'www.chaoyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('div.center-title::text').get(),
            'date': response.css('div.fl::text').get(),
            'content': response.css('div.center-info  ::text').getall(),
            'source': response.css('body > div.main-wrap > div.wrap > div > div.center-info > div > div::text').get(),
        }
