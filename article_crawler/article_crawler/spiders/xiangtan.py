from article_crawler.baseSpider import baseSpider


class XiangtanSpider(baseSpider):
    name = 'xiangtan'

    @baseSpider.parser('xiangtan', 'www.xiangtan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('div.ftheme::text').get(),
            'date': response.css('div.flot-ly > span:nth-child(2)::text').re('：(.*)'),
            'source': response.css('div.ffxar2-1 > span::text').re('：(.*)'),
            'content': response.css('#zoom  ::text').getall(),
        }

    @baseSpider.parser('xiangtan', 'www.xiangtan.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('div.details-tit > h2::text').get(),
            'date': '无',
            'source': response.css('#list > div > div.details-con > table.details-table.table-line.t2 > tbody > tr:nth-child(5) > td:nth-child(2)::text').get(),
            'content': response.css('#list > div > div.details-con > table.details-table.table-line.t2 > tbody > tr:nth-child(2) > td:nth-child(4)::text').get(),
        }

    @baseSpider.parser('xiangtan', 'xttj.xiangtan.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'title': response.css('#ivs_title::text').get(),
            'date': response.css('div.ewb-sources > span:nth-child(2)::text').re('：(.*)'),
            'source': response.css('div.ewb-laiyuan > span.w3').re('：(.*)'),
            'content': response.css('#zoom  ::text').getall(),
        }

    @baseSpider.parser('xiangtan', 'www.xiangtan.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'title': response.css('div.xlnk > h2::text').get(),
            'date': response.css('div.xlnk > h6 > span:nth-child(2)::text').re('：(.*)'),
            'source': response.css('div.xlnk > h6 > span:nth-child(1)::text').get(),
            'content': response.css('div.xl-xqnr  ::text').getall(),
        }

