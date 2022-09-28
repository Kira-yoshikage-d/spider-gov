#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tqdm

from pymongo import MongoClient
from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError
from scrapy.utils.project import get_project_settings
from csv import DictWriter

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

class Command(ScrapyCommand):
    def short_desc(self):
        return "下载数据"


    def run(self, args, opts):
        if len(args) != 1:
            raise UsageError()

        client = MongoClient(get_project_settings().get('MONGODB_URI'))


        total_num: int = client['scrapy_gov'][args[0]].count_documents(
            filter={
                'content': {
                    '$exists': True
                }
            }
        )

        print(f"{total_num} documents found.")

        result = client['scrapy_gov'][args[0]].aggregate([
            {
                '$match': {
                    'content': {
                        '$exists': True
                    }
                }
            }, {
                '$set': {
                    'keywords': {
                        '$reduce': {
                            'input': '$info', 
                            'initialValue': '', 
                            'in': {
                                '$concat': [
                                    '$$this.keyword', ' ', '$$value'
                                ]
                            }
                        }
                    }, 
                    'date': {
                        '$getField': {
                            'field': 'date', 
                            'input': {
                                '$first': '$info'
                            }
                        }
                    }, 
                    'city': {
                        '$getField': {
                            'field': 'city', 
                            'input': {
                                '$first': '$info'
                            }
                        }
                    }
                }
            }, {
                '$project': {
                    'title': 1, 
                    '_id': 0, 
                    'url': 1, 
                    'date': 1, 
                    'keywords': {
                        '$trim': {
                            'input': '$keywords'
                        }
                    }, 
                    'content': 1, 
                    'city': 1
                }
            }
        ])

        with open(file="data/download/{0}.csv".format(args[0]), mode="w", encoding="utf-8") as f:
            csv_writer = DictWriter(f, fieldnames=['city', 'title', 'keywords', 'date', 'content', 'url'])
            csv_writer.writeheader()
            with tqdm.tqdm(total=total_num, miniters=1, desc="downloading", colour='green') as pbar:
                for item in result:
                    csv_writer.writerow(item)
                    pbar.update(1)

        print("downloaded into data/download/{0}.csv".format(args[0]))
