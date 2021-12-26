# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ProductItem

def process_item_list_request(request: Request):
    return request

def use_splash(request: Request):
    script = """
                function main(splash, args)
                    splash.images_enabled = false
                    splash.js_enabled = true
                    assert(splash:go{args.url, headers=args.headers})
                    splash:wait(3)
                    return {
                        html = splash:html()
                    }
                end
            """
    request.meta['splash'] = {
                'endpoint':'execute',
                'args':{
                    'wait': 15,
                    'lua_source': script
                    }
                }
    return request

class CelineChinaSpider(CrawlSpider):
    name = 'celine_china'
    allowed_domains = ['www.celine.cn']
    start_urls = [
        'https://www.celine.cn/celine-men',
        'https://www.celine.cn/celine-women'
    ]

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths='//a[@class="component-top-categories-herotext"]'
        ), process_request=process_item_list_request),
        Rule(LinkExtractor(
            restrict_xpaths='//a[@class="component-category__item-btn--view-all"]'
        ), process_request=process_item_list_request),
        Rule(LinkExtractor(
            restrict_xpaths='//a[@class="component-product__item-link"]'
        ), callback='parse_item', process_request=use_splash),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url)
                        
    def parse_item(self, response):
        if re.search('https://www.celine.cn/CONF.+', response.url):
            item = ProductItem()
            item['url'] = response.url
            item['name'] = response.xpath('normalize-space(//div[@class="component-products-right__name"]/text())').get()
            item['price'] = response.xpath('normalize-space(//div[@class="component-products-right__price font-neueBold mb-28"]/text())').get()
            return item
