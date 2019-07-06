# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from __future__ import absolute_import

import pyscore

from pymongo import MongoClient
from scrapy.conf import settings

keywords = ["roadtrek", "miles", "generator", "condition"]
tagged_keywords = pyscore.tag_list(keywords)


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

    def score_item(self, statement):
        score = 0
        score += pyscore.MatchExact(keywords, statement)
        score += pyscore.MatchNLP(tagged_keywords, statement)

        return score

    def process_item(self, item, spider):
        found_item = self.collection.find_one({"link": item['link']})
        # found_item = None

        if found_item == None:

            item['score'] = self.score_item(
                item['description'])

            print(item)
            self.collection.insert_one(item)

        return item


if __name__ == "__main__":
    testItem = {}
    testItem['link'] = 'somelink.com'
    testItem['description'] = 'some thing condition'
    testItem['listingTitle'] = 'some title'

    pipeline = MongoDBPipeline()
    processed_item = pipeline.process_item(testItem, None)
