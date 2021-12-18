# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import Buyma


class BuymaSpiderSpider(scrapy.Spider):
    name = 'buyma_spider'
    allowed_domains = ['buyma.com']
    start_urls = ['https://www.buyma.com/r/']

    def parse(self, response):
        posts = response.xpath('.//*[@class="product "]')
        for post in posts:
            item = Buyma()

            item["name"] = post.xpath('.//div[@class="product_name"]/a/text()').get()
            item["price"] = post.xpath('.//span[@class="Price_Txt"]/text()').get()
            url = post.xpath('.//div[@class="product_name"]/a/@href').get()
            item["url"] = "https://www.buyma.com" + url

            yield item


        # If there is a next button on this page, move the crawler
        next_page_url = response.xpath('//a[@rel="next"]/@href').get()
        abs_next_page_url = response.urljoin(next_page_url)
        if abs_next_page_url is not None:
            yield Request(abs_next_page_url, callback=self.parse)
