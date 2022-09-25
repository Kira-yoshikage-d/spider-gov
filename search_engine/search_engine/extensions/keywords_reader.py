#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from scrapy.utils import project
from typing import List

class KeywordsReader:
    def __init__(self, keywords_set: str = '') -> None:
        with open("keywords.json", mode="rt", encoding='utf8') as f:
            keywords_sets = json.load(f)
        if not keywords_set:
            settings = project.get_project_settings()
            keywords_set = settings.get('SEARCH_ENGINE_KEYWORDS_SET')
        self.keywords = keywords_sets.get(keywords_set)

    def __getitem__(self, key: str):
        keywords_str = self.keywords.get(key, self.keywords.get('default'))
        if not keywords_str:
            raise Exception("not in keywords_set")
        return keywords_str.split("、")

