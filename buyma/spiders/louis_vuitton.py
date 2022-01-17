# -*- coding: utf-8 -*-
import scrapy


class LouisVuittonSpider(scrapy.Spider):
    name = 'louis_vuitton'
    allowed_domains = ['jp.louisvuitton.com']
    start_urls = ['http://jp.louisvuitton.com/']

    def parse(self, response):
        pass
