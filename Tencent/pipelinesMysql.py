# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import pymysql
from scrapy.conf import settings

# Mysql

class TencentPipeline(object):
    # 保存数据

    def __init__(self):
        self.host = settings['MYSQL_HOST']
        self.user = settings['MYSQL_USER']
        self.pwd = settings['MYSQL_PWD']
        self.db = settings['MYSQL_DB']
        self.charset = settings['MYSQL_CHARSET']
        self.port = int(settings['MYSQL_PORT'])
        self.table = settings['MYSQL_TABLE']
        self.conn = pymysql.connect(host=self.host, user=self.user,passwd=self.pwd, db=self.db, charset=self.charset, port=self.port)

    def open_spider(self, spider):
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into {0}({1}) values ({2})".format(self.table, ','.join(item.keys()), ','.join(['%s'] * len(item.fields.keys())))
        # print(tuple(item.values()))
        self.cur.execute(sql, tuple(item.values()))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()



