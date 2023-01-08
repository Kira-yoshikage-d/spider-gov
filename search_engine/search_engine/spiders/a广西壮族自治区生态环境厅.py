from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A广西壮族自治区生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '广西壮族自治区生态环境厅'
    api: str = 'http://sthjt.gxzf.gov.cn/igs/front/search.jhtml?position=TITLE&timeOrder=desc&code=0f9498493ccd4d3eb6b2d1acbb4418c8&orderBy=time&pageSize=10&type=&time=&pageNumber={page}&sortByFocus=true&siteId=275&sitename=%E8%87%AA%E6%B2%BB%E5%8C%BA%E7%94%9F%E6%80%81%E7%8E%AF%E5%A2%83%E5%8E%85&sitetype=%E8%87%AA%E6%B2%BB%E5%8C%BA%E9%83%A8%E9%97%A8&name=%E8%87%AA%E6%B2%BB%E5%8C%BA%E7%94%9F%E6%80%81%E7%8E%AF%E5%A2%83%E5%8E%85&siteclass=%E7%94%9F%E6%80%81%E7%8E%AF%E5%A2%83&searchWord={keyword}'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        return int(response.json()["page"]["totalPages"])

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.json()["page"]["content"]

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
        if item.get("DOCTITLE", "unknown") is 'unknown':
            result = {
                'title': item.get("title", "unknown"),
                'url': item.get("url", "unknown"),
                'source': item.get("trs_site", "unknown"),
                'date': item.get("trs_time", "unknown"),
            }
        else:
            result = {
                'title': item.get("DOCTITLE", "unknown"),
                'url': item.get("url", "unknown"),
                'source': item.get("SITENAME", "unknown"),
                'date': item.get("PUBDATE", "unknown"),
            }
        return result

