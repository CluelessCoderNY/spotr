# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient
from scrapy.conf import settings


class MongoDBPipeline(object):

    def __init__(self):
        try:
            connection = MongoClient(
                settings['MONGODB_SERVER'],
                settings['MONGODB_PORT'])
            db = connection[settings['MONGODB_DB']]
            self.collection = db[settings['MONGODBdb_COLLECTION']]
        except:
            connection = MongoClient(
                "localhost",
                27017)
            db = connection["spotr"]
            self.collection = db["posts"]

    def process_item(self, item, spider):
        found_item = self.collection.find_one({"link": item['link']})

        if found_item == None:
            self.collection.insert_one(item)

        return item


if __name__ == "__main__":
    testitem = {}
    testitem['link'] = 'somelink.com'

    pipeline = MongoDBPipeline()
    processed_item = pipeline.process_item(testitem, None)
