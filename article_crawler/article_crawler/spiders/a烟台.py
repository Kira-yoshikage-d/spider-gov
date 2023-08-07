from article_crawler.baseSpider import baseSpider


class A烟台Spider(baseSpider):
    name = '烟台'

    @baseSpider.parser('烟台', 'www.yantai.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall(),
        }
