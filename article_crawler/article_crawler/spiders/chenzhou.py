from article_crawler.baseSpider import baseSpider


class ChenzhouSpider(baseSpider):
    # TODO
    name = 'chenzhou'

    @baseSpider.parser('chenzhou', 'czggzy.cz.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('div.title  ::text').getall(),
            'date': response.css('span.time::text').get(),
            'source': response.css('span.origin::text').get(),
            'content': response.css('div#zoom  ::text').getall(),
        }

    @baseSpider.parser('chenzhou', 'czj.czs.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('div.xlnk h2::text').get(),
            'date': response.css('div.xlnk h6 > span:nth-child(1)::text').get(),
            'source': response.css('div.xlnk h6 > span:nth-child(2)::text').get(),
            'content': response.css('div.xl-xqnr  ::text').getall(),
        }

    @baseSpider.parser('chenzhou', 'www.czs.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'title': response.css('div.zhengcebiaoti::text').get(),
            'date': response.css('div.fabushijian::text').get(),
            'source': response.css('div.fabulaiyuan::text').get(),
            'content': response.css('div#zoom  ::text').getall()
        }

    @baseSpider.parser('chenzhou', 'www.czs.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'title': response.css('div.nrbt::text').get(),
            'date': response.css('div.xnrbt::text').re('发布时间：(.*?)\xa0{4}')[0],
            'source': response.css('div.xnrbt::text').re('信息来源：(.*?)\xa0{4}')[0],
            'content': response.css('div#zoom  ::text').getall()
        }

    @baseSpider.parser('chenzhou', 'www.czs.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'title': response.css('h1::text').get(),
            'date': response.css(
                'body > div:nth-child(3) > div > div.desc > table > tr > td > table > tr > td:nth-child(1)::text').re(
                r'日期：([\s\S]*?)\xa0')[0],
            'source': response.css(
                'body > div:nth-child(3) > div > div.desc > table > tr > td > table > tr > td:nth-child(1)::text').re(
                r'来源：([\s\S]*?)\xa0')[0],
            'content': response.css('div#zoom  ::text').getall()
        }

    @baseSpider.parser('chenzhou', 'czggzy.cz.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'title': response.css('div.title  ::text').getall(),
            'date': response.css('div.info-box > span:nth-child(2)::text').get(),
            'source': response.css('div.info-box > span:nth-child(1)::text').get(),
            'content': response.css('div.content  ::text').getall(),
        }

    @baseSpider.parser('chenzhou', 'czggzy.cz.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'title': response.css('div.detail-ltitle::text').get(),
            'date': response.css('div.detailinfo-left.f-left > span:nth-child(3)::text').get(),
            'source': '政务公开',
            'content': response.css('div#zoom  ::text').getall(),
        }

    @baseSpider.parser('chenzhou', 'www.czs.gov.cn')
    def parser_8(self, response, **kwargs):
        return {
            'title': response.css('div.zhengcebiaoti::text').get(),
            'date': response.css('div.zhengcelistbg > ul > li::text').re('登记日期：(.*)')[0],
            'source': response.css('div.zhengcelistbg > ul > li::text').re('公开责任部门：(.*)')[0],
            'content': response.css('div#zoom  ::text').getall(),
        }

    @baseSpider.parser('chenzhou', 'czs.gov.cn')
    def parser_8(self, response, **kwargs):
        return {
            'title': response.css('div.sub-article > h2::text').get(),
            'date': response.css('div.sub-article > h6 > label::text').re('发布时间：(.*)')[0],
            'source': response.css('div.sub-article > h6 > label::text').re('信息来源：(.*)')[0],
            'content': response.css('div#div_content  ::text').getall(),
        }

    @baseSpider.parser('chenzhou', 'anrenzf.gov.cn')
    def parser_9(self, response, **kwargs):
        return {
            'title': response.css('div.details-tit > h2::text').get(),
            'date': '无',
            'source': response.css('#list > div.details > div.details-con > table.details-table.table-line.t2 > '
                                   'tr:nth-child(5) > td:nth-child(2)::text').get(),
            'content': response.css('#list > div.details > div.details-con > table.details-table.table-line.t1 > '
                                    'tr > td.each-show::text').getall(),
        }
