from article_crawler.baseSpider import baseSpider


class A北京生态环境局Spider(baseSpider):
    name = '北京生态环境局'

    @baseSpider.parser('北京生态环境局', 'http://sthjj.beijing.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.h_dl_c p::text").getall()
        }
