from article_crawler.baseSpider import baseSpider


class A唐山Spider(baseSpider):
    name = '唐山'

    @baseSpider.parser('唐山', 'new.tangshan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#conN  :not(script):not(style)::text").getall()
        }
