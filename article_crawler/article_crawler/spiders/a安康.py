from article_crawler.baseSpider import baseSpider


class a安康Spider(baseSpider):
    name = "安康"

    @baseSpider.parser("安康", "http://www.ankang.gov.cn")
    def parser_1(self, response, **kwargs):
        return {
            "content": response.css(
                "div#fontzoom  ::text"
            ).getall(),
        }

    @baseSpider.parser("安康", "http://www.ankang.gov.cn")
    def parser_3(self, response, **kwargs):
        return {
            "content": response.css("section  :not(script):not(style)::text").getall(),
        }

    @baseSpider.parser("安康", "http://www.ankang.gov.cn")
    def parser_4(self, response, **kwargs):
        return {
            "content": response.css("#fontzoom::text").get(),
        }
