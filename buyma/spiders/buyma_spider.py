# -*- coding: utf-8 -*-
import scrapy
from ..items import Buyma


class BuymaSpiderSpider(scrapy.Spider):
    name = 'buyma_spider'
    allowed_domains = ['buyma.com']
    start_urls = ['https://www.buyma.com/r/-C3260/']

    def parse(self, response):
        for post in response.xpath('//li[@class="product "]'):

            yield Buyma(
                url=post.xpath('//div[@class="product_Action"]/@item-url').extract(),
                name=post.xpath('//div[@class="product_name"]/a/text()').extract(),
                price=post.xpath('//span[@class="Price_Txt"]/text()').extract(),
                brand=post.xpath('//a[@class="brandname"]//text()').extract(),
                shopper=post.xpath('//div[@class="product_Buyer"]/a//text()').extract(),
            )

        return
