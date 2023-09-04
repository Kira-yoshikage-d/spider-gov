from article_crawler.baseSpider import baseSpider


class A天津生态环境局Spider(baseSpider):
    name = '天津生态环境局'

    @baseSpider.parser('天津生态环境局', 'https://sthj.tj.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            "content": response.css("div.TRS_PreAppend p::text").getall()
        }


