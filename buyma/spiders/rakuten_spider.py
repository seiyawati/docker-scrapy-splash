# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import Rakuten


class RakutenSpiderSpider(scrapy.Spider):
    name = 'rakuten_spider'
    allowed_domains = ['https://brandavenue.rakuten.co.jp/']
    start_urls = [
        'https://brandavenue.rakuten.co.jp/all-sites/cateb-0000000013/catem-0000000003/men/?l-id=brn_men_category'
        ]

    def parse(self, response):
        posts = response.xpath('.//*[@class="tlb_list_item tlb_clearfix tlb_productList searchList"]/li')
        for post in posts:
            item = Rakuten()

            item["name"] = post.xpath('.//div/a/img[@class="searchLazy image active"]/@alt').get()
            item["price"] = post.xpath('.//p[@class="tlb_text"]/span[contains(@class, "price")]/text()').get()
            item["brand"] = post.xpath('.//p[@class="tlb_text"]/span[contains(@class, "brand")]/text()').get()
            # url = post.xpath('//div[@class="product_name"]/a/@href')[i].get()
            # item["url"] = "https://www.buyma.com" + url

            yield item