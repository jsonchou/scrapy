# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

__author__ = 'jsonchou'

import scrapy


class DianzanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tieba_name = scrapy.Field()
    tieba_link = scrapy.Field()
    tieba_pic = scrapy.Field()
    level1 = scrapy.Field()
    level2 = scrapy.Field()
    level3 = scrapy.Field()
    member_num = scrapy.Field()
    chat_num = scrapy.Field()
    tieba_desc = scrapy.Field()
