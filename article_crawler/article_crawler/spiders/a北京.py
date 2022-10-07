from article_crawler.baseSpider import baseSpider


class A北京Spider(baseSpider):
    name = '北京'

    @baseSpider.parser('北京', 'cgj.beijing.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#zoom  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://credit.bjchp.gov.cn/add/article?id=news_4a947423-540f-43ba-9949-27b149802b0f')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.article-mail-txt  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://csglw.beijing.gov.cn/sdhjjs/sdhjjsgzdt/201912/t20191204_838736.html')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("#div_zhengwen  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("div.xl_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css("div.xl_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css("#mainText  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css("div.article_i  :not(script):not(style)::text").getall()
        }
