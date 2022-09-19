from article_crawler.baseSpider import baseSpider


class A衡水Spider(baseSpider):
    name = '衡水'

    @baseSpider.parser('衡水', 'www.hengshui.gov.cn')
    def parser_1(self, response, **kwargs):
        result = {
            'content': response.css("#barrierfree_container > div.neirong > div > div.nr_P > p  ::text").getall()
        }
        return result
