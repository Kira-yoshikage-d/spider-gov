from article_crawler.baseSpider import baseSpider


class a开封Spider(baseSpider):
    name = '开封'

    @baseSpider.parser('开封', 'www.kaifeng.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('font#zoom  ::text').getall(),
        }
    @baseSpider.parser('开封', 'www.kaifeng.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('td > div.zoomTY::text').getall()
        }

    @baseSpider.parser('开封', 'www.kaifeng.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('div.artCon  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('开封', 'www.kaifeng.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css(' body > table > tbody > tr > td > div.zoomTY  ::text').get(),
        }
    
    @baseSpider.parser('开封', 'www.kaifeng.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css('td > font#zoom::text').get(),
        }