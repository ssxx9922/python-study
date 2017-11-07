# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    status = scrapy.Field()
    people = scrapy.Field()

    toUser = scrapy.Field()
    priopity = scrapy.Field()
    fromUser = scrapy.Field()
    lookUser = scrapy.Field()
    product = scrapy.Field()

    taskId = scrapy.Field()
    
