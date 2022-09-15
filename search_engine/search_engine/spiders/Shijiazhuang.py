from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class ShijiazhuangSpider(ZhengFuBaseSpider):
    name: str = 'Shijiazhuang'
    token_url = 'https://www.sjz.gov.cn/so/s?qt={keyword}&siteCode=1301000003&tab=all&toolsStatus=1'
    api = 'https://api.so-gov.cn/s'
    method: str = 'POST'
    debug: bool = False
    custom_settings: Optional[dict] = {
        'DOWNLOADER_MIDDLEWARES': {
            'search_engine.middlewares.WordTokenDownloaderMiddleware': 543,
        },
        'COOKIES_ENABLED': False,
        'DOWNLOAD_DELAY': 1,
    }

    def edit_page(self, response):
        # inspect_response(response, self)
        raw_data = response.json()
        total_items_num = raw_data["data"]["search"]["totalHits"]
        total_page = int(total_items_num) // 20 + 1
        return total_page

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data["data"]["search"]["searchs"]
        return items_box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        result = {
            "title": item.get("title", ""),
            "url": item.get("viewUrl", ""),
            "date": item.get("docDate", ""),
            "source": item.get("siteName", ""),
            "type": item.get("displayDb", ""),
        }
        return result

