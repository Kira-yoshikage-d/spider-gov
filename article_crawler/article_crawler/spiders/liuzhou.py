from article_crawler.baseSpider import baseSpider


class LiuzhouSpider(baseSpider):
    name = 'liuzhou'

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'title': response.css('#bar h3.marginB25::text').get(),
            'date': response.css('#bar span::text').re(r'发布日期：([\s\S]*)')[0],
            'source': response.css('#bar span::text').re(r'信息来源：([\s\S]*)')[0],
            'content': response.css('#zoom > div:nth-child(1)  ::text').getall(),
        }

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'title': response.css('#bar h3.marginB15::text').get(),
            'date': response.css('div.contentBox span::text').re(r'发布日期：([\s\S]*)')[0],
            'source': response.css('div.contentBox span::text').re(r'来源：([\s\S]*)')[0],
            'content': response.css('div.contentBox div.contentTextBox > div:nth-child(1)  ::text').getall(),
        }

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'title': response.css('#bar h3.marginB25::text').get(),
            'date': response.css('#bar span::text').re(r'发布日期：([\s\S]*)')[0],
            'source': '新闻中心',
            'content': response.css('#zoom > div:nth-child(1)  ::text').getall(),
        }

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'title': response.css('#PC > div.content > div.mainDetails > div > div.fileLibraryBox.clearfix > dl:nth-child(5) > dd::text').get(),
            'date': response.css('#PC > div.content > div.mainDetails > div > div.fileLibraryBox.clearfix > dl:nth-child(7) > dd::text').get(),
            'source': response.css('#PC > div.content > div.mainDetails > div > div.fileLibraryBox.clearfix > dl:nth-child(3) > dd::text').get(),
            'content': response.css('#zoom > div:nth-child(1)  ::text').getall(),
        }

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'title': response.css('#bar h3.marginB25::text').get(),
            'date': response.css('#bar span::text').re(r'发布日期：([\s\S]*)')[0],
            'source': '新闻中心',
            'content': response.css('div.contentTextBox > div:nth-child(1)  ::text').getall(),
        }

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'title': response.css('#PC h3.marginB25::text').get(),
            'date': response.css('#PC span::text').re('发布日期：(.*)'),
            'source': response.css('#PC span::text').re('来源：(.*)'),
            'content': response.css('#zoom > div:nth-child(1)  ::text').getall(),
        }

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'title': response.css('#PC h3.marginB25::text').get(),
            'date': response.css('#PC span::text').re('发布日期：(.*)'),
            'source': '无',
            'content': response.css('#zoom > div:nth-child(1)  ::text').getall(),
        }

    @baseSpider.parser('liuzhou', 'www.liuzhou.gov.cn')
    def parser_8(self, response, **kwargs):
        return {
            'title': response.css('#bar h3.marginB25::text').get(),
            'date': response.css('#bar span::text').re(r'发布日期：([\s\S]*)')[0],
            'source': response.css('#bar span::text').re(r'信息来源：([\s\S]*)')[0],
            'content': response.css('#zoom  :not(div)::text').getall(),
        }

