# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html


# useful for handling different item types with a single interface

from search_engine.middlewares.downloaderMiddlewares import WordTokenDownloaderMiddleware
from search_engine.middlewares.scrapy_mongodb import MongoDBPipeline
