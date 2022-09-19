#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError
from scrapy.utils import project
from scrapy.spiderloader import SpiderLoader


class Command(ScrapyCommand):
    def short_desc(self):
        return "用于调试旧爬虫."

    def run(self, args, opts):
        if len(args) == 1:
            spider_name = args[0]
            debug = True
        elif len(args) == 2:
            spider_name = args[0]
            debug = False
        else:
            raise UsageError()

        spidercls = SpiderLoader.from_settings(project.get_project_settings()).load(spider_name)
        spidercls.debug = debug
        spidercls.crawler_process = self.crawler_process

        self.crawler_process.crawl(spidercls)
        self.crawler_process.start()


