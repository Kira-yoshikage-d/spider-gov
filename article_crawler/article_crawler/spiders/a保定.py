from article_crawler.baseSpider import baseSpider


class A保定Spider(baseSpider):
    name = '保定'

    @baseSpider.parser('保定', 'www.baoding.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("body > div.sj_nrbr > table.sj_nr > tr > td  ::text").getall()
        }
