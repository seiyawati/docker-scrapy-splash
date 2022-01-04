# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Buyma(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()

class Rakuten(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()

class Books(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    detail_page_url = scrapy.Field()

class ProductItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
