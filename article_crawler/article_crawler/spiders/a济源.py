from article_crawler.baseSpider import baseSpider


class A济源Spider(baseSpider):
    name = '济源'

    @baseSpider.parser('济源', 'http://jyj.jiyuan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  p::text").getall()
        }

    @baseSpider.parser('济源', 'www.jiyuan.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.content  p::text").getall()
        }

    @baseSpider.parser('济源', 'http://gkw.jiyuan.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.con-detail  p::text").getall()
        }

    @baseSpider.parser('济源', 'http://czjrj.jiyuan.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("div.TRS_Editor  p::text").getall()
        }

    @baseSpider.parser('济源', 'http://zrzyghj.jiyuan.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css("div.content  p::text").getall()
        }

    @baseSpider.parser('济源', 'http://zrzyghj.jiyuan.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css("div.content  p::text").getall()
        }

    @baseSpider.parser('济源', 'http://nmj.jiyuan.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css("div.content  p::text").getall()
        }

    @baseSpider.parser('济源', 'http://hbj.jiyuan.gov.cn')
    def parser_8(self, response, **kwargs):
        return {
            'content': response.css("div.content div.TRS_UEDITOR ::text").getall()
        }

    @baseSpider.parser('济源', 'http://gkw.jiyuan.gov.cn')
    def parser_9(self, response, **kwargs):
        return {
            'content': response.css("div.con-detail p::text").getall()
        }

    @baseSpider.parser('济源', 'http://fgw.jiyuan.gov.cn')
    def parser_10(self, response, **kwargs):
        return {
            'content': response.css("div.content p::text").getall()
        }
