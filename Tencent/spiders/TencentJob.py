# -*- coding: utf-8 -*-
import logging


import scrapy

from Tencent.items import TencentItem


class TencentjobSpider(scrapy.Spider):
    
    # 功能
    # 爬取腾讯社招信息
    name = 'TencentJob'
    allowed_domains = ['tencent.com']
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    # 起始地址
    start_urls = [url+str(offset)]

    def parse(self, response):
        for row in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化对象模型
            item = TencentItem()
            # 职位名称
            item["position_name"] = (row.xpath("./td[1]/a/text()").extract() or [''])[0]
            # 详情连接
            item["position_link"] = (row.xpath("./td[1]/a/@href").extract() or [''])[0]
            # 职位类别
            item["position_type"] = (row.xpath("./td[2]/text()").extract() or [''])[0]
            # 招聘人数
            item["people_num"] = (row.xpath("./td[3]/text()").extract() or [''])[0]
            # 工作地点
            item["work_location"] = (row.xpath("./td[4]/text()").extract() or [''])[0]
            # 发布时间
            item["pub_time"] = (row.xpath("./td[5]/text()").extract() or [''])[0]

            yield item

        # 3316
        if self.offset < 3316:
            self.offset += 10

        yield scrapy.Request(self.url+str(self.offset), callback=self.parse)
