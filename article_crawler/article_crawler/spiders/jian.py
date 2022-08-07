from article_crawler.baseSpider import baseSpider


class JianSpider(baseSpider):
    name = 'jian'

    @baseSpider.parser('jian', 'agri.jian.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('h1.aTitle::text').get(),
            'date': '无',
            'source': response.css('div.luru_c > span::text').re(r'来源：(.*?)\xa0')[0],
            'content': response.css('#content  ::text').getall(),
        }

    @baseSpider.parser('jian', 'agri.jian.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('#barrierfree_container\  > div > div.zwxxgk_box > div.Rcont.zn_cont > div > table > tbody > '
                                  'tr:nth-child(3) > td.txt::text').get(),
            'date': response.css('#barrierfree_container\  > div > div.zwxxgk_box > div.Rcont.zn_cont > div > table > tbody > '
                                 'tr:nth-child(2) > td:nth-child(4)::text').get(),
            'source': response.css('#barrierfree_container\  > div > div.zwxxgk_box > div.Rcont.zn_cont > div > table > tbody > '
                                   'tr:nth-child(2) > td:nth-child(2)::text').get(),
            'content': response.css('div.xxgk_content  ::text').getall()
        }

    @baseSpider.parser('jian', 'czj.jian.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'title': response.css('div.text-title::text').get(),
            'date': response.css('div.information-list.fl::text').get(),
            'source': response.css('div.information-list.fl > span::text').re('来源：(.*)')[0],
            'content': response.css('div.text-main  ::text').getall(),
        }

    @baseSpider.parser('jian', 'www.jian.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'title': response.css('div.show_title::text').get(),
            'date': response.css('div.show_ziduan > span > span::text').re('发布时间：(.*)')[0],
            'source': response.css('div.show_ziduan > span > span::text').re('来源：(.*)')[0],
            'content': response.css('div#font_size1  ::text').getall(),
        }

    @baseSpider.parser('jian', 'www.jian.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'title': response.css('#barrierfree_container\  > div.zwxxgk_bd > div.zwxxgk_box > div.Rcont.zn_cont > div > table > tbody > '
                                  'tr:nth-child(3) > td.txt::text').get(),
            'date': response.css('#barrierfree_container\  > div.zwxxgk_bd > div.zwxxgk_box > div.Rcont.zn_cont > div > table > tbody > '
                                 'tr:nth-child(2) > td:nth-child(4)::text').get(),
            'source': response.css('#barrierfree_container\  > div.zwxxgk_bd > div.zwxxgk_box > div.Rcont.zn_cont > div > table > tbody > '
                                   'tr:nth-child(1) > td:nth-child(4)::text').get(),
            'content': response.css('div.WordSection1  ::text').getall(),
        }

    @baseSpider.parser('jian', 'czj.jian.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'title': response.css('div.text-title::text').get(),
            'date': response.css('div.information-list.fl::text').get(),
            'source': response.css('div.text-main strong::text').re('来源：(.*)')[0],
            'content': response.css('div.text-main  ::text').getall(),
        }

    @baseSpider.parser('jian', 'sl.jian.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'title': response.css('h1.post-title::text').get(),
            'date': response.css('div.postmeta > p::text').re(r'时间：(.*?)\xa0')[0],
            'source': response.css('div.postmeta > p::text').re(r'来源：(.*)')[0],
            'content': response.css('div.entry  ::text').getall(),
        }

    @baseSpider.parser('jian', 'czj.jian.gov.cn')
    def parser_8(self, response, **kwargs):
        return {
            'title': response.css('div.text-title::text').get(),
            'date': response.css('div.information-list.fl::text').get(),
            'source': response.css('div.information-list.fl > span::text').re('发布者：(.*)')[0],
            'content': response.css('div.text-main  ::text').getall(),
        }

