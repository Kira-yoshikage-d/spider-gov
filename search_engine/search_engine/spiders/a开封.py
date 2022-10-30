from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A开封Spider(ZhengFuBaseSpider):
    name: str = '开封'
    api: str = 'http://www.kaifeng.gov.cn/searchEngine.do?offset=1'
    method: str = 'POST'
    data: dict[str, Any] = {
        'fkToken004': '45a83180411848ae88a4796f3910392f',
        'siteidIndex': 0,
        'cititleIndex': '{keyword}',
        'cidocumentcategoryIndex': '',
        'cidocumentyearIndex': '',
        'cidocumentnumberIndex': '',
        'cxareacodeIndex': '',
        'cxyearnumberIndex': '',
        'cxindexIndex': '',
        'cicontentIndex': '{keyword}'
    }
    debug: bool = False
    # custom_settings: Optional[dict] = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'search_engine.middlewares.WordTokenDownloaderMiddleware': 543,
    #     },
    #     'COOKIES_ENABLED': False,
    #     'DOWNLOAD_DELAY': 0.5,
    # }
    # token_url = 'http://sthjj.beijing.gov.cn/so/s?qt={keyword}&siteCode=1100000122&tab=all&toolsStatus=1'

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        raise NotImplementedError()

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        raise NotImplementedError()

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
            # 'title': ,
            # 'url': ,
            # 'source': ,
            # 'date': ,
        }
        return result

