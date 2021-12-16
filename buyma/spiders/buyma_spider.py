# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import Buyma


class BuymaSpiderSpider(scrapy.Spider):
    name = 'buyma_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books = response.xpath('.//*[@class="product_pod"]')
        for book in books:
            item = Buyma()

            item["title"] = book.xpath('.//h3/a/@title').get()
            item["price"] = book.xpath('.//*[@class="price_color"]/text()').get()
            img_url = book.xpath('.//*[@class="image_container"]/a/@href').get()
            item["detail_page_url"] = "http://books.toscrape.com/" + img_url

            yield item


        # If there is a next button on this page, move the crawler
        next_page_url = response.xpath('//a[text()="next"]/@href').get()
        abs_next_page_url = response.urljoin(next_page_url)
        if abs_next_page_url is not None:
            yield Request(abs_next_page_url, callback=self.parse)
