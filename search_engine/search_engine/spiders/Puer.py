import base64

import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class PuerSpider(ZhengFuBaseSpider):
    """IP 反爬"""
    name = 'Puer'
    allowed_domains = ['puershi.gov.cn']
    method = "POST"
    api = "http://www.puershi.gov.cn/zhjsjgy.jsp"
