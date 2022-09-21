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
        return self.keywords.get(key).split("、")

