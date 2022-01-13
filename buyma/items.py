# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class Buyma(Item):
    name = Field()
    price = Field()
    url = Field()

class Books(Item):
    title = Field()
    price = Field()
    detail_page_url = Field()

class ProductItem(Item):
    url = Field()
    name = Field()
    price = Field()
    image = Field()
