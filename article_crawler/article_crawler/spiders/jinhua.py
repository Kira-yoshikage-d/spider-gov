from article_crawler.baseSpider import baseSpider


class JinhuaSpider(baseSpider):
    name = 'jinhua'

    @baseSpider.parser('jinhua', 'jinhua.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('div.jh_xl_m1 > h1::text').get(),
            'date': response.css('div.jh_xl_c1 > span::text').re(r'发布日期：([\S\s]*)')[0],
            'source': response.css('#source::text').re(r'来源：([\S\s]*)')[0],
            'content': response.css('div.jh_xl_m2  ::text').getall(),
        }

    @baseSpider.parser('jinhua', 'jinhua.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('body > div.content > div.article > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)::text').get(),
            'date': response.css('body > div.content > div.article > div > div > table > tbody > tr:nth-child(5) > td:nth-child(2)::text').get(),
            'source': response.css('body > div.content > div.article > div > div > table > tbody > tr:nth-child(4) > td:nth-child(2)::text').get(),
            'content': response.css('body > div.content > div.article > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > p::text').get(),
            'reply': response.css('body > div.content > div.article > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > p::text').get()
        }
