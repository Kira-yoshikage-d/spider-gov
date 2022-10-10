from article_crawler.baseSpider import baseSpider


class A北京Spider(baseSpider):
    name = '北京'

    @baseSpider.parser('北京', 'cgj.beijing.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#zoom  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://credit.bjchp.gov.cn/add/article?id=news_4a947423-540f-43ba-9949-27b149802b0f')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div.article-mail-txt  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://csglw.beijing.gov.cn/sdhjjs/sdhjjsgzdt/201912/t20191204_838736.html')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("#div_zhengwen  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("div.xl_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css("div.xl_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css("#mainText  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css("div.article_i  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_8(self, response, **kwargs):
        return {
            'content': response.css("div.view.TRS_UEDITOR.trs_paper_default.trs_web  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_9(self, response, **kwargs):
        return {
            'content': response.css("div.mycontont  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_10(self, response, **kwargs):
        return {
            'content': response.css("div.content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_11(self, response, **kwargs):
        return {
            'content': response.css("#ggzw > font  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_12(self, response, **kwargs):
        return {
            'content': response.css("div.detail-desc  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_13(self, response, **kwargs):
        return {
            'content': response.css("div.xiangqing  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_14(self, response, **kwargs):
        return {
            'content': response.css("div.article  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_15(self, response, **kwargs):
        return {
            'content': response.css("div#fontzoom  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_16(self, response, **kwargs):
        return {
            'content': response.css("div.overview  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_17(self, response, **kwargs):
        return {
            'content': response.css("div.easysite-news-text  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_18(self, response, **kwargs):
        return {
            'content': response.css("div.nrtxt  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('北京', 'http://fgw.beijing.gov.cn/fgwzwgk/zcgk/sjbmgfxwj/gjfgwwj/202004/t20200420_1847539.htm')
    def parser_19(self, response, **kwargs):
        return {
            'content': response.css("div.detailContent  :not(script):not(style)::text").getall()
        }
