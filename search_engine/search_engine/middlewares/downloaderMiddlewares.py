#!/usr/bin/env python
# -*- coding: utf-8 -*-
import termcolor
import logging
from scrapy import Request, Spider, Selector, FormRequest
from scrapy.responsetypes import Response

from search_engine.basepro import ZhengFuBaseSpider

import requests
from typing import List, Optional, Tuple
from time import sleep

from scrapy.spiders import signals


class PubProperty:
    token_url: str = "http://www.beijing.gov.cn/so/s?tab=all&siteCode=1100000088&qt={keyword}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    def __init__(self, keyword: str, token_url: str='') -> None:
        self._keyword = keyword
        self.token_url = token_url
        self.reinit(keyword=keyword)

    def _init(self, *args) -> None:
        _attrs = ['siteCode', 'tab', 'qt', 'debug', 'page', 'pageSize', 'timestamp', 
                  'wordToken', 'tabToken', 'tagParam', 'apiUrl', 'auto', 'multiSelect', 'suid']
        for key, val in zip(_attrs, args):
            setattr(self, key, val)

    def __repr__(self) -> str:
        return 'PubProperty Object with suid: ' + str(getattr(self, 'suid'))

    @staticmethod
    def parse_args(response: requests.Response) -> List[str]:
        selector = Selector(text=response.text)
        args_list: List[str] = [s.strip().replace("'", "").replace(",", "").split(".")[0] 
                                for s in selector.css("script::text").re(r'initPubProperty\(([\s\S]*?)\);')[0].strip().split('\r\n')]
        return args_list

    def reinit(self, keyword: Optional[str]=None):
        if not keyword:
            keyword = self._keyword
        response = requests.get(self.token_url.format(keyword=keyword), headers=self.headers)
        args_list = self.parse_args(response=response)
        self._init(*args_list)
        return self

    @property
    def query_info(self) -> Tuple[dict[str, str], dict[str, str]]:
        fields = ['siteCode', 'tab', 'timestamp', 'wordToken', 'page', 'pageSize', 'qt']
        data = { field: str(getattr(self, field)) for field in fields }
        data['pageSize'] = '20'
        data['sort'] = 'relevance'
        data['timeOption'] = '0'
        data['keyPlace'] = '0'
        data['fileType'] = ''
        headers: dict[str, str] = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
            'suid': getattr(self, 'suid'),
        }
        return data, headers

class WordTokenDownloaderMiddleware:
    token_cache: dict[str, PubProperty] = {}

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        cls.logger = logging.getLogger("scrapy-wordToken-downloadMiddleware")
        return s
        
    def spider_opened(self, spider: ZhengFuBaseSpider):
        for keyword in spider.keywords:
            self.token_cache[keyword] = PubProperty(keyword=keyword, token_url=spider.token_url)
            sleep(1)

    def process_request(self, request: FormRequest, spider: Spider):
        page, keyword = request.meta['page'], request.meta['keyword']
        formdata, headers = self.token_cache[keyword].query_info
        formdata['page'] = str(page)
        s = request.replace(
            formdata=formdata,
            meta={'keyword': keyword, 'formdata': formdata, 'page': page, 'processed': True},
            headers=headers,
        )
        request._body, request.headers = s._body, s.headers
        return None

    def process_response(self, request: Request, response: Response, spider: Spider):
        try:
            data = response.json()
        except Exception as e:
            self.logger.debug(str(e))
            ok = False
        else:
            ok = data['ok']

        if ok:
            return response
        else:
            page, keyword = request.meta['page'], request.meta['keyword']
            reason: str = data.get("msg", "unknown")

            self.logger.debug(termcolor.colored(f"{keyword}: 第{page}页 not ok, refetching token...", "yellow"))
            self.logger.debug(termcolor.colored(f"reason: {reason}", "yellow"))

            pub_property = self.token_cache[keyword].reinit()

            self.logger.debug(termcolor.colored(f"{keyword}: {page} refetching done!"), "yellow")

            formdata, headers = pub_property.query_info
            formdata['page'] = str(page)

            s = request.replace(
                formdata=formdata,
                meta={'keyword': keyword, 'formdata': formdata, 'page': page, 'processed': True},
                headers=headers
            )

            return s

