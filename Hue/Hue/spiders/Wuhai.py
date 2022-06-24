from copy import copy

import scrapy
from fake_useragent import UserAgent
from scrapy import FormRequest

ua = UserAgent()


class WuhaiSpider(scrapy.Spider):
    name = 'Wuhai'
    allowed_domains = ['wuhai.gov.cn']
    start_urls = ['http://www.wuhai.gov.cn/']
    api = "http://www.wuhai.gov.cn/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60"
    debug = False
    data = {
        "originalSearchUrl": "/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60",
        "originalSearch": "",
        "app": "2d2145bfde734f20b3a746f5040a2752,b46547d5770e4c1794e9a337836ba34d,ab217b6d91d64085bd05924b218abbc8,4536d378b2a843d79ad0cbb2d5433ce1,fcff548c7a114dd3b3970d3866191820",
        "appName": "",
        "sr": "score desc",
        "advtime": "",
        "advrange": "",
        "ext": "-siteId:1",
        "pNo": "",
        "searchArea": "",
        "advtime": "",
        "advrange": "",
        "advepq": "",
        "advoq": "",
        "adveq": "",
        "searchArea": "",
        "advSiteArea": "",
        "q": "",
    }

    def start_requests(self):
        """起始点"""
        keywords = self.keywords
        if not keywords:
            raise Exception("No Keywords Provided!")
        for keyword in keywords:
            req = FormRequest(
                    url = self.api,
                    formdata = self.build_form_data(keyword=keyword),
                    headers = {"User-Agent": ua.random},
                    callback = self.parse_index
                    )
            req.cb_kwargs["keyword"] = keyword
            req.cb_kwargs["page"] = 1
            yield req

    def parse_index(self, response, keyword, page):
        """解析 index 页"""
        yield from self.parse_items(response, keyword, page)
        page = self.parse_page(response)
        # 爬取剩余页
        for p in range(2, page+1):
            form_data = self.build_form_data(page=p, keyword=keyword)
            req = FormRequest(
                    url = self.api,
                    formdata = form_data,
                    headers = {"User-Agent": ua.random},
                    callback = self.parse_items
                    )
            req.cb_kwargs["keyword"] = keyword
            req.cb_kwargs["page"] = p
            self.logger.info("rong-ning 爬取 查询页面 关键字:{} 页数:{}".format(keyword, p))
            yield req

    def parse_page(self, response):
        """解析总页数"""
        page = response.css("#panel-page > div > div.jcyh-lbys > div.default-result-list-paging > span > span::text").get()
        return int(page)


    def parse_items(self, items, keyword=None, page=None):
        items_box = items.css("div.default-result-list > div.searchMod")
        return (self.parse_item(item, keyword, page) for item in items_box)


    def parse_item(self, item, keyword, page):
        """解析meta信息"""
        meta_info = {
            "title": ''.join(item.css("div.news-style1 > h3 > a::text, div.news-style1 > h3 > a > font::text").getall()).strip(),
            "pre_content": ''.join(item.css("p.txtCon::text, p.txtCon > font::text").getall()).strip(),
            "url": item.css("p.dates > a::attr(href)").get(),
            "date": item.css("p.dates > span::text").get(),
            "keyword": keyword,
            "page": page
        }
        return meta_info

    def build_form_data(self, page=None, keyword=None, **kwargs):
        """构造表单数据"""
        form_data = copy(self.data)
        if page:
            form_data['pNo'] = str(page)
        if keyword:
            form_data['q'] = keyword
        form_data |= kwargs
        return form_data



