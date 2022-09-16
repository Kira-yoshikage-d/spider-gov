from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class ZhumadianSpider(ZhengFuBaseSpider):
    """TODO 搜索接口不同"""
    name = 'zhumadian'
    api = 'https://www.zhumadian.gov.cn/plus/seek/index.php?currpage={page}&pagesize=20&skey={keyword}'
    api_start = 'https://www.zhumadian.gov.cn/plus/seek/index.php?skey={keyword}&texttype=1'
    method = 'GET'

    custom_settings = {
        "RETRY_HTTP_CODES": [500, 502, 503, 504, 522, 524, 408, 429, 301, 302],
        "DOWNLOADER_MIDDLEWARES": {
            'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,
        }
    }

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        item_num = int(response.css("#pp > table > tbody > tr > td:nth-child(8) > span::text").get())
        page_num = item_num // 20 + 1
        return page_num

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        box = response.css("div.box1_result")

    def edit_items(self, items_box: Selector) -> Selector:
        """
        将目录索引整理为标准迭代器.
        """
        divs = items_box.css("div")
        for index in range(20):
            base_index = 3 * index
            yield (divs[base_index], divs[base_index+1], divs[base_index+2])

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        data = {}
        div_title_selector, _, div_nav_selector = item
        data['title'] = ''.join(div_title_selector.css("a  ::text").getall())
        data['url'] = div_title_selector.css("a::attr(href)").get()
        data['date'] = div_title_selector.css("::text").get()
        data['source'] = ''.join(div_nav_selector.css("a::text").getall())
        return data

