# -*- coding: utf-8 -*-
import logging
import scrapy
import urllib.parse

from urllib import parse

from Dianzan.items import DianzanItem


class DianzanSpider(scrapy.Spider):

    # 功能
    # 贴吧
    name = 'Dianzan'
    allowed_domains = ['baidu.com']
    url = "http://tieba.baidu.com/f/index/forumpark?cn=北京院校&ci=0&pcn=高等院校&pci=0&ct=1&rn=20&pn="
    offset = 1
    # 起始地址
    start_urls = [url+str(offset)]

    def parse(self, response):
        level1 = response.xpath("//div[@class='ba_class_title']/text()").extract() or ['']
        level2 = response.xpath("//a[@class='cur_class']/text()").extract() or ['']
        rows = response.xpath("//div[@id='ba_list']/div[starts-with(@class,'ba_info')]/a")
        for row in rows:
            # 初始化对象模型
            item = DianzanItem()
           
            # 贴吧名称
            item["tieba_name"] = (row.xpath("./div/p[@class='ba_name']/text()").extract() or [''])[0]
            # 贴吧地址
            item["tieba_link"] = urllib.parse.unquote((row.xpath('@href').extract() or [''])[0])
            # 贴吧图片地址
            item["tieba_pic"] = (row.xpath("./img[@class='ba_pic']/@src").extract() or [''])[0]
            # 一级类别
            item["level1"] = level1[0]
            # 二级类别
            item["level2"] = level2[0]
            # 三级类别
            item["level3"] = 0
            # 会员人数
            item["member_num"] =  int((row.xpath("./div/p/span[@class='ba_m_num']/text()").extract() or [''])[0])
            # 帖子数量
            item["chat_num"] =  int((row.xpath("./div/p/span[@class='ba_p_num']/text()").extract() or [''])[0])
            # 简述
            item["tieba_desc"] =  (row.xpath("./div/p[@class='ba_desc']/text()").extract() or [''])[0]

            yield item

        # 30
        if self.offset <= 1:
            self.offset += 1

        yield scrapy.Request(self.url+str(self.offset), callback=self.parse)
