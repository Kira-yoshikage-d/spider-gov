from article_crawler.baseSpider import baseSpider


class XuanchengSpider(baseSpider):
    name = 'xuancheng'

    @baseSpider.parser('xuancheng', 'www.xuancheng.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('body > div.is-main > div.m-main.container > div.row.f-mlrf7 > div.com-md-8.col-lg-9.f-plr7.m-review > div > table:nth-child(2) > tbody > tr:nth-child(1) > td.u-td2::text').get(),
            'date': response.css('body > div.is-main > div.m-main.container > div.row.f-mlrf7 > div.com-md-8.col-lg-9.f-plr7.m-review > div > table:nth-child(2) > tbody > tr:nth-child(3) > td.u-td2::text').get(),
            'source': '市长信箱',
            'content': response.css('body > div.is-main > div.m-main.container > div.row.f-mlrf7 > div.com-md-8.col-lg-9.f-plr7.m-review > div > table:nth-child(2) > tbody > tr:nth-child(2) > td.u-td2.u-main-detail  ::text').get(),
            'reply': response.css('body > div.is-main > div.m-main.container > div.row.f-mlrf7 > div.com-md-8.col-lg-9.f-plr7.m-review > div > table:nth-child(4) > tbody > tr:nth-child(2) > td.u-td2.u-main-detail2  ::text').getall()
                   + response.css('body > div.is-main > div.m-main.container > div.row.f-mlrf7 > div.com-md-8.col-lg-9.f-plr7.m-review > div > table:nth-child(5) > tbody > tr:nth-child(2) > td.u-td2.u-main-detail2  ::text').getall(),
        }

    @baseSpider.parser('xuancheng', 'www.xuancheng.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('#title::text').get(),
            'date': response.css('div.u-wzinfo > span:nth-child(1)::text').re('：(.*)'),
            'source': response.css('div.u-wzinf > span:nth-child(2)::text').re('：(.*)'),
            'content': response.css('#zoom  ::text').getall(),
        }

    @baseSpider.parser('xuancheng', 'www.xuancheng.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'title': response.css('div.text-center.u-title::text').get(),
            'date': response.css('div.text-center.u-desc.f-mb20 > span:nth-child(1)::text').re('：(.*)'),
            'source': response.css('div.text-center.u-desc.f-mb20 > span:nth-child(2)::text').re('：(.*)'),
            'content': response.css('#zoom  ::text').getall(),
        }

    @baseSpider.parser('xuancheng', 'www.xuancheng.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'title': response.css('h1.u-dttit::text').get(),
            'date': response.css('body > div.is-main > div > div > section.m-opendetail > div.m-detailinfo.f-mb14 > ul > li:nth-child(4) > div::text').get(),
            'source': response.css('body > div.is-main > div > div > section.m-opendetail > div.m-detailinfo.f-mb14 > ul > li:nth-child(8) > div::text').get(),
            'content': response.css('#zoom  ::text').getall(),
        }
