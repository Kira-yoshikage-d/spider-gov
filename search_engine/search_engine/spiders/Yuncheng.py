from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class YunchengSpider(ZhengFuBaseSpider):
    name: str = 'Yuncheng'
    api: str = 'https://www.yuncheng.gov.cn/search2/api/select'
    method: str = 'POST'
    allowed_domains: List[str] = ['www.yuncheng.gov.cn']
    headers: dict[str, str] = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
    }
    data: dict[str, Any] = {
        "q": "SITE_ID:1 AND TITLE:{keyword}  NOT CHANNEL_ROOT:辅助栏目",
        "fq": "STATUS:4 AND DEL_FLAG:false",
        "fl": "TITLE,CONTENT,CHANNEL_ROOT,SITE_ID,CHANNEL_PATH,CHANNEL_ID_PATH,MOD_TIME,STATUS,WRITE_TIME,SITE_NAME,URL,PIC_URL,ID,DOC_ID,SUMMARY,KIND,CHAN_ID,DEL_FLAG,KIND,DEPT_NAME,DOMAIN,URL2",
        "start": "20",
        "rows": "20",
        "CHANNEL_ROOT": "",
        "sort": "score desc,SORT desc",
        "facet": "true",
        "pageNum": "{page}",
        "facet.mincount": "1",
        "facet.limit": "10",
        "facet.field": "DEL_FLAG",
        "hl": "true",
        "hl.fl": "TITLE,CONTENT",
        "hl.id": "ID",
        "hl.simple.pre": "<em>",
        "hl.simple.post": "</em>",
        "hl.maxAnalyzedChars": "-1",
        "hl.fragsize": "120",
        "hl.usePhraseHighlighter": "true",
        "hl.highlightMultiTerm": "true",
    }
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        data = response.json()
        return int(data["facet_counts"]["facet_fields"]["DEL_FLAG"]["false"]) // 20 + 1

    def edit_data(self, data: dict, keyword: str, page: int, **kwargs) -> dict[str, Any]:
        data['start'] = 20 * (page - 1)
        return data

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        data = response.json()
        return data["response"]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item["TITLE"],
            'url': item["URL"],
            'source': item["CHANNEL_PATH"],
            'date': item["MOD_TIME"],
        }
        return result

