import scrapy
import copy
from scrapy import Request, FormRequest


class ZhengFuBaseSpider(scrapy.Spider):
    name = ''
    allowed_domains = ['']
    start_urls = ['']
    # 关键字
    keywords = []
    # API
    api = ""
    # 模式 GET/POST
    mode = "default"
    data = {}
    data_page_key = ""
    data_keyword_key = ""
    # 测试用 headers
    headers = {"User-Agent": "Google Bot"}
    # 解析items_box
    parse_items_box = ""
    # 解析item
    parse_item = ""
    parse_item_data = {}
    # 解析page
    parse_page = ""

    def start_requests(self):
        """
        抛出初始请求
        """
        # 验证关键字存在
        keywords = self.keywords
        if not keywords:
            raise Exception("Need keywords!")

        # 验证API存在
        api = self.api
        if not api:
            raise Exception("Need API!")

        # 检查模式: 有data就是POST模式，否则是GET模式
        data = self.data
        if not data:
            self.mode = "GET"
        else:
            if not self.data_keyword_key or not self.data_page_key:
                raise Exception("Need meta of data!")
            self.mode = "POST"

        # 判断mode
        mode = self.mode
        if mode == "defualt":
            raise Exception("Need a Mode!")

        if mode == "GET":
            yield from self.start_get_requests(self)
        elif mode == "POST":
            yield from self.start_post_requests(self)
        else:
            raise Exception("Unknown Error on mode!")

    def start_get_requests(self, page=None, callback=None):
        keywords = self.keywords
        api = self.api
        headers = self.headers
        if not page:
            page = 1
        if not callback:
            callback = self.parse_index
        for keyword in keywords:
            url = api.format(keyword=keyword, page=page)
            req = Request(
                url=url,
                headers=headers,
                callback=self.parse_index
                )
            yield req

    def start_post_requests(self, page=None, callback=None):
        keywords = self.keywords
        url = self.api
        headers = self.headers
        data = copy.copy(self.data)
        if not page:
            page = "1"
        else:
            page = str(page)
        if not callback:
            callback = self.parse_index
        for keyword in keywords:
            data[self.data_keyword_key] = keyword
            data[self.data_page_key] = page
            req = FormRequest(
                url=url,
                headers=headers,
                formdata=data,
                callback=callback
            )
            yield req

    def parse_index(self, response):
        # 解析第一页
        yield from self.parse_items(response)
        # 获取总页数
        total_page = self.parse_total_page(response)
        # 抛出余下页的请求
        if self.mode == "GET":
            for page in range(2, total_page+1):
                yield from self.start_get_requests(page, self.parse_items)
        elif self.mode == "POST":
            for page in range(2, total_page+1):
                yield from self.start_post_requests(page, self.parse_items)

    def parse_items(self, response):
        """
        从index_response中解析items_box
        """
        parse_items_box = self.parse_items_box
        if not parse_items_box:
            raise Exception("Must rewrite parse_items")
        items_box = self.parse_g(response, parse_items_box)
        yield from self.parse_item(items_box)

    def parse_item(self, items_box):
        """
        具体的解析每个item的逻辑，抛出dict
        """
        parse_item = self.parse_item
        if not parse_item:
            raise Exception("Must rewrite parse_item")
        items = self.parse_g(items_box, parse_item)
        for item in items:
            # 初始化data
            data = self.parse_item_data(item)
            yield data

    def parse_total_page(self, response):
        """
        解析总共的页数
        """
        parse_page = self.parse_page
        if not parse_page:
            raise Exception("Must rewrite parse_total_page")
        return int(self.parse_g(response, parse_page).get())

    def parse_g(self, response, parse_string):
        if "/" in parse_string:
            return response.xpath(parse_string)
        else:
            return response.css(parse_string)

    def parse_item_data(item):
        """
        return: dict
        """
        raise Exception("Must rewrite parse_item_data")
