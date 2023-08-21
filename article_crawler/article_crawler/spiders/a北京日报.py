from article_crawler.baseSpider import baseSpider


class A北京日报Spider(baseSpider):
    name = '北京日报'

    @baseSpider.parser('北京日报', 'ie.bjd.com.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.content2 div.storyContent p::text").getall()
        }

    @baseSpider.parser('北京日报', 'bjrbdzb.bjd.com.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("#content p::text").getall()
        }

    @baseSpider.parser('北京日报', 'kw.beijing.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("td.bt_content p::text").getall()
        }

    @baseSpider.parser('北京日报', 'bj.bjd.com.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("div.storyContent p::text").getall()
        }

    @baseSpider.parser('北京日报', 'www.bjchp.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css("#zoom p::text").getall()
        }

    @baseSpider.parser('北京日报', 'kfqgw.beijing.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css("#div_zhengwen p::text").getall()
        }


    @baseSpider.parser('北京日报', 'www.bjft.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css("#div_zhengwen p::text").getall()
        }

    @baseSpider.parser('北京日报', 'www.bjdch.gov.cn')
    def parser_8(self, response, **kwargs):
        return {
            'content': response.css("#mainText p::text").getall()
        }



