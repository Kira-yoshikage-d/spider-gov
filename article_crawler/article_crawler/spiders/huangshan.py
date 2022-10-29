from article_crawler.baseSpider import baseSpider


class HuangshanSpider(baseSpider):
    name = 'huangshan'

    @baseSpider.parser('huangshan', 'www.huangshan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('h1.wztit::text').get(),
            'date': response.css('span.fbsj::text').re('发布时间：(.*)')[0],
            'source': response.css('span.res::text').re('信息来源：(.*)')[0],
            'content': response.css('div.wzcon.j-fontContent  ::text').getall(),
        }

    @baseSpider.parser('huangshan', 'www.huangshan.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('h1.wztit::text').get(),
            'date': response.css('span.fbsj::text').re('发布时间：(.*)')[0],
            'source': response.css('span.aut::text').re('作者：(.*)')[0],
            'content': response.css('div.wzcon.j-fontContent  ::text').getall(),
        }

