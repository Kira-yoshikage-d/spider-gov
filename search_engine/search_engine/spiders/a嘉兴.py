import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class JiaxingSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '嘉兴'
    api = "https://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do"
    headers = {
        "Cookie": " __jsluid_h=3934a1690556b58ff8921ccac8496085; __jsl_clearance=1667006408.782|0|Ubx5mnWnWkxA%2FoZ04bFQRycbBhI%3D; __jsluid_s=1880770df3ebf98ce094697511c99728; __jsl_clearance_s=1667006410.57|0|8iyLjAuamG0v9CEhPnQrmhUDEsU%3D; yfx_c_g_u_id_10006944=_ck22102909201513931517511749755; yfx_f_l_v_t_10006944=f_t_1667006415390__r_t_1667006415390__v_t_1667006415390__r_c_0; hefei_gova_SHIROJSESSIONID=af6e0615-828c-40b9-ac00-d7c3395f3a72",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
    }
    method = "POST"
    start_urls = ['http://www.zj.gov.cn//']
    debug = False

    data = {
        "websiteid": "330401000000000",
        "pg": "10",
        "p": "1",
        "tpl": "2296",
        "cateid": "370",
        "isContains": "0",
        "q": "价格",
        "sortType": "1"
    }

    def edit_data(self, data, keyword, page):
        data["word"] = str(keyword)
        data["current"] = str(page)
        return data

    def edit_items_box(self, response):
        return response.json().get('result')

    def edit_item(self, item):
        data = {}
        urllink = "https://search.zj.gov.cn/jrobotfront/"
        data['url'] = urllink+item.css("div.titleWrapper > a::attr(href)").get()
        data['type'] = item.css("div.titleWrapper > input.tagclass::attr(value)").get()
        data['title'] = item.css("div.titleWrapper > a::text").getall()
        data['source'] = item.css("div.sourceTime >span:nth-child(1)::text").get()
        data['date'] = item.css("div.sourceTime >span:nth-child(2)::text ").get()
        return data

    def edit_items(self, items_box):
        return [Selector(text=item) for item in items_box]

    def edit_page(self, response):
        raw_data = response.json()
        total_page_num = raw_data.get("total", 0)
        return int(total_page_num)//10+1

