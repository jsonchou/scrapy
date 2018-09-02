# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import sqlite3

# SQLite

class TencentPipeline(object):
    # 保存数据

    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE'),
            sqlite_table=crawler.settings.get('SQLITE_TABLE', 'items')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into {0}({1}) values ({2})".format(self.sqlite_table, ','.join(item.keys()), ','.join(['?'] * len(item.fields.keys())))
        print(tuple(item.values()))
        self.cur.execute(sql, tuple(item.values()))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


# con.executemany("insert into person(firstname, lastname) values (?, ?)", persons)
