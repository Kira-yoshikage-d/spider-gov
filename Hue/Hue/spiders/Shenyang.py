import re
import time

import requests
import scrapy
from Hue.basepro import ZhengFuBaseSpider
from scrapy.shell import inspect_response

token_rex = re.compile(
    pattern="initPubProperty\(.*?attrs",
    flags=re.S
    )


class ShenyangSpider(ZhengFuBaseSpider):
    """POST
    TODO token 反爬"""
    name = 'Shenyang'
    api = 'https://api.so-gov.cn/s'
    token_api = 'http://www.shenyang.gov.cn/so/s?qt={keyword}&siteCode=2101000053&tab=all&toolsStatus=1'
    method = "POST"
    token_cache = {}
    data = {
        "siteCode": "2101000053",
        "tab": "all",
        "timestamp": "{timestamp}",
        "wordToken": "{wordtoken}",
        "page": "{page}",
        "pageSize": "20",
        "qt": "{keyword}",
        "timeOption": "0",
        "sort": "relevance",
        "keyPlace": "0",
        "fileType": "",
    }
    parse_first = False

    def edit_data(self, data, keyword, page):
        if keyword not in self.token_cache:
            self.logger.info("Get wordToken of {}".format(keyword))
            token_resp = requests.get(self.token_api.format(keyword=keyword))
            self.logger.info(token_resp.cookies)
            token = token_rex.search(token_resp.text).group().split()[-3]
            token = token.split("'")[1]
            self.token_cache[keyword] = token
        data["wordToken"] = self.token_cache[keyword]
        data["qt"] = str(keyword)
        data["page"] = str(page)
        data["timestamp"] = str(time.time_ns())[:13]
        return data

    def edit_page(self, response):
        # inspect_response(response, self)
        raw_data = response.json()
        total_items_num = raw_data["data"]["search"]["totalHits"]
        total_page = int(total_items_num) // 20 + 1
        return total_page

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data["data"]["search"]["searchs"]
        yield items_box

    def edit_items(self, items_box):
        for item in items_box:
            yield item
