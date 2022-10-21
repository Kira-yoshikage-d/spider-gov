#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from scrapy.utils import project
from typing import Dict, List

class KeywordsReader:
    def __init__(self, keywords_set: str = '') -> None:
        with open("keywords.json", mode="rt", encoding='utf8') as f:
            keywords_sets = json.load(f)
        if not keywords_set:
            settings = project.get_project_settings()
            keywords_set = settings.get('SEARCH_ENGINE_KEYWORDS_SET')
        if keywords_set == 'ALL':
            self.keywords = self.get_all_keywords(keywords_sets)
            return
        self.keywords = keywords_sets.get(keywords_set)

    def __getitem__(self, key: str):
        keywords_str = self.keywords.get(key, self.keywords.get('default'))
        if not keywords_str:
            raise Exception("not in keywords_set")
        return keywords_str.split("、")

    @staticmethod
    def get_all_keywords(keywords_set: Dict[str, Dict[str, str]]) -> Dict[str, str]:
        all_keywords_dict = {}
        for d in keywords_set.values():
            for k, v in d.items():
                if k in all_keywords_dict:
                    all_keywords_dict[k] = '、'.join([all_keywords_dict[k], v])
                else:
                    all_keywords_dict[k] = v
        return all_keywords_dict
