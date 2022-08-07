from article_crawler.baseSpider import baseSpider
from scrapy.responsetypes import Response


class LasaSpider(baseSpider):
    name = 'lasa'

    @baseSpider.parser('lasa', 'www.lasa.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('div.detail > h1::text').get(),
            'date': '{}年{}月{}日 {}'.format(
                response.css('p.yyyy::text').get(),
                response.css('p.mmdd::text').get().split('/')[0],
                response.css('p.mmdd::text').get().split('/')[1],
                response.css('p.hhmm::text').get()
            ),
            'source': response.css('p.source::text').get(),
            'content': response.css('#NewsContent  ::text').getall(),
        }

    @baseSpider.parser('lasa', 'www.lasa.gov.cn')
    def parser_2(self, response: Response, **kwargs):
        date = response.url.split('/')[5]
        return {
            'title': response.css('div.zfxxgk_content > h2::text').get(),
            'date': date[:4] + '年' + date[4:] + '月',
            'source': '政府信息公开',
            'content': response.css('div.zfxxgk_content  ::text').getall()
        }

    @baseSpider.parser('lasa', 'www.lasa.gov.cn')
    def parser_3(self, response: Response, **kwargs):
        return \
            {
            'title': response.css('hd_xjxq > h1::text').get(),
            'date': response.css('body > div.container > div > div.hd_xjxq > form > div.group1 > div:nth-child(2) > span::text').get(),
            'source': '市长信箱',
            'content': response.css('body > div.container > div > div.hd_xjxq > form > div:nth-child(3) > div > span > p::text').get(),
            'reply': response.css('body > div.container > div > div.hd_xjxq > form > div:nth-child(6) > div > span > p::text').getall(),
        }

    @baseSpider.parser('lasa', 'www.lasa.gov.cn')
    def parser_4(self, response: Response, **kwargs):
        return {
            'title': response.css('#cnet-top > h4::text').get(),
            'date': response.css('#cnet-top > p::text').re(r'发布时间：(.*?)\xa0')[0],
            'source': response.css('#cnet-top > p::text').re(r'来源：(.*?)\xa0')[0],
            'content': response.css('#cnet  ::text').getall(),
        }