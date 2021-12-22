# -*- coding: utf-8 -*-
import scrapy


class CelineChinaSpider(scrapy.Spider):
    name = 'celine_china'
    allowed_domains = ['www.celine.cn']
    start_urls = ['http://www.celine.cn/']

    def parse(self, response):
        pass
