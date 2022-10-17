from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class JiaozuoSpider(ZhengFuBaseSpider):
    name: str = '焦作'
    api: str = 'http://www.jiaozuo.gov.cn/search/SolrSearch/searchData'
    method: str = 'POST'
    debug: bool = False
    data = {
        'q': '{keyword}',
        'catalogId': '',
        'type': '',
        'allWord': '',
        'noWord': '',
        'timeType': '',
        'sort': '',
        'order': '',
        'forCatalogType': '0',
        'token4': '4243bdcb86554de0b1ba92050a3365df',
        'siteId': '',
        'offset': '{page}',
        'limit': '8',
        'infoType': ''
    }

    # custom_settings: Optional[dict] = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'search_engine.middlewares.WordTokenDownloaderMiddleware': 543,
    #     },
    #     'COOKIES_ENABLED': False,
    #     'DOWNLOAD_DELAY': 0.5,
    # }
    # token_url = 'http://www.jiaozuo.gov.cn/search/SolrSearch/s'

    def edit_data(self, data: dict, keyword: str, page: int, **kwargs) -> dict[str, Any]:
        data['offset'] = int((page-1) * 8)
        return data

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        return int(response.json()["totalPage"])

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["rows"]

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            "title": item.get("articleTitle", ""),
            "url": "http://www.jiaozuo.gov.cn" + item.get("articleUri", ""),
            "date": item.get("articlePublishTime", ""),
            "source": item.get("siteName", ""),
            "type": item.get("catalogName", ""),
        }
        return result

