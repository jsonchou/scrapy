# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import pymongo
from scrapy.conf import settings

# MongoDB


class DianzanPipeline(object):
    # 保存数据

    def __init__(self):
        user = settings['MONGO_USER']
        pwd = settings['MONGO_PWD']

        host = settings['MONGO_HOST']
        port = int(settings['MONGO_PORT'])
        db = settings['MONGO_DB']
        coll = settings['MONGO_COLL']

        self.client = pymongo.MongoClient(host=host, port=port)
        # self.client.admin.authenticate(user, pwd)
        self.db = self.client[db]  # 获得数据库的句柄
        self.coll = self.db[coll]  # 获得collection的句柄

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        data = dict(item)
        self.coll.insert(data)
        return item

    def close_spider(self, spider):
        pass
