#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from scrapy.http.request.json_request import JsonRequest as OriginJsonRequest

class JsonRequest(OriginJsonRequest):
    def __init__(self, *args, formdata: dict, dumps_kwargs: Optional[dict] = None, **kwargs) -> None:
        super().__init__(*args, data=formdata, dumps_kwargs=dumps_kwargs, **kwargs)
