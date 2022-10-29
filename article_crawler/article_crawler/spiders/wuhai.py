from article_crawler.baseSpider import baseSpider


class WuhaiSpider(baseSpider):
    name = 'wuhai'

    @baseSpider.parser('wuhai', 'www.wuhai.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('div.wh_xl_t::text').get(),
            'date': response.css('#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(4)::text').get(),
            'source': response.css('#ly::text').re('来源：(.*)'),
            'content': response.css('#wh_x_c  ::text').getall(),
        }

    @baseSpider.parser('wuhai', 'shuiwuju.wuhai.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('div.wh_xl_t::text').get(),
            'date': response.css('div.wh_xl_z > span:nth-child(1)::text').re('发布时间：(.*)'),
            'source': response.css('#ly::text').re('来源：(.*)'),
            'content': response.css('#wh_x_c  ::text').getall(),
        }

    @baseSpider.parser('wuhai', 'wjw.wuhai.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'title': response.css('div.wh_xl_t::text').get(),
            'date': response.css('div.wh_xl_z > span:nth-child(1)::text').re('发布时间：(.*)'),
            'source': response.css('#ly::text').get(),
            'content': response.css('#zoom  ::text').getall(),
        }

    @baseSpider.parser('wuhai', 'www.wuhai.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'title': response.css('h2.title::text').get(),
            'date': response.css('div.intro > span:nth-child(1)::text').re('：(.*)'),
            'source': '乌海市人民政府',
            'content': response.css('#zoom  ::text').getall(),
        }

    @baseSpider.parser('wuhai', 'www.wuhai.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'title': response.css('#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(2) > td:nth-child(2)::text').get(),
            'date': response.css('#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(6) > td:nth-child(2)::text').get(),
            'source': '事件投诉',
            'content': response.css('#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(3) > td:nth-child(2)::text').get(),
            'reply': response.css('#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(9) > td:nth-child(2)::text').get(),
        }

    @baseSpider.parser('wuhai', 'www.wuhai.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'title': response.css('div.wh_xl_t::text').get(),
            'date': response.css('#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(4)::text').get(),
            'source': response.css('#ly::text').re('来源：(.*)'),
            'content': response.css('#wh_x_c  ::text').getall(),
        }

    @baseSpider.parser('wuhai', 'www.wuhai.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'title': response.css('#8d96a5112f1e40a69d83bacd39a6eaaf > div:nth-child(2) > div.detail > table > tbody > tr:nth-child(2) > td:nth-child(2)::text').get(),
            'date': '无',
            'source': response.css('#8d96a5112f1e40a69d83bacd39a6eaaf > div:nth-child(2) > div.detail > table > tbody > tr:nth-child(4) > td:nth-child(2)::text').get(),
            'content': response.css('#8d96a5112f1e40a69d83bacd39a6eaaf > div:nth-child(2) > div.detail > table > tbody > tr:nth-child(5) > td:nth-child(2)  ::text').getall(),
        }

    @baseSpider.parser('wuhai', 'www.wuhai.gov.cn')
    def parser_8(self, response, **kwargs):
        return {
            'title': response.css(
                '#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(2) > td:nth-child(2)::text').get(),
            'date': response.css(
                '#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(5) > td:nth-child(2)::text').get(),
            'source': '事件投诉',
            'content': response.css(
                '#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(3) > td:nth-child(2)::text').get(),
            'reply': response.css(
                '#32613577ba2e45f98e384bd877713119 > div:nth-child(2) > div.wh_xl > div.wh_xl_m > table > tbody > tr:nth-child(9) > td:nth-child(2)::text').get(),
        }

