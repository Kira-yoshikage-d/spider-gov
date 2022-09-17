# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from search_engine.middlewares.scrapy_mongodb import MongoDBPipeline


class search_enginePipeline:
    config = {
        'unique_key': []
    }

    def open_spider(self, spider):
        settings = spider.settings
        if settings['MONGODB_UNIQUE_KEY']:
            self.config['unique_key'] = settings['MONGODB_UNIQUE_KEY']

    def process_item(self, item, spider):
        keys = self.config['unique_key']
        adjusted_item = {k: item.get(k, '') for k in keys}
        item_others = {k: item.get(k, '') for k in item if k not in keys}
        adjusted_item['info'] = item_others
        return adjusted_item


