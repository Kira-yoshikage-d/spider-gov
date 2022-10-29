import scrapy
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class QuzhouSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '衢州'
    headers = {
        "Cookie": " __jsluid_h=3934a1690556b58ff8921ccac8496085; __jsl_clearance=1667006408.782|0|Ubx5mnWnWkxA%2FoZ04bFQRycbBhI%3D; __jsluid_s=1880770df3ebf98ce094697511c99728; __jsl_clearance_s=1667006410.57|0|8iyLjAuamG0v9CEhPnQrmhUDEsU%3D; yfx_c_g_u_id_10006944=_ck22102909201513931517511749755; yfx_f_l_v_t_10006944=f_t_1667006415390__r_t_1667006415390__v_t_1667006415390__r_c_0; hefei_gova_SHIROJSESSIONID=af6e0615-828c-40b9-ac00-d7c3395f3a72",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
    }
    debug = False

    allowed_domains = ['qz.gov.cn', 'zj.gov.cn']
    start_urls = ['http:///www.qz.gov.cn//']
    api = "https://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do"
    method = "POST"
    data = {
        "q": "{keyword}",
        "websiteid": "330801000000000",
        "pg": "10",
        "tpl": "2296",
        "Municipal_webid": "330801000000000",
        "cateid": "370",
        "sortType": "1",
        "p": "{page}"
    }

    def edit_data(self, data: dict, keyword: str, page: int):
        data["q"] = keyword
        data["p"] = str(page)
        return data

    def edit_page(self, response: Response) -> int:
        total_num = int( response.json().get("total") )
        return total_num // 10 + 1

    def edit_items_box(self, response: Response):
        return response.json().get('result')

    def edit_items(self, items_box):
        return [Selector(text=item) for item in items_box]

    def edit_item(self, item):
        data = {}
        urllink = "https://search.zj.gov.cn/jrobotfront/"
        data['url'] = urllink+item.css("div.titleWrapper > a::attr(href)").get()
        data['type'] = item.css("div.titleWrapper > input.tagclass::attr(value)").get()
        data['title'] = item.css("div.titleWrapper > a::text").getall()
        data['source'] = item.css("div.sourceTime >span:nth-child(1)::text").get()
        data['date'] = item.css("div.sourceTime >span:nth-child(2)::text ").get()
        return data