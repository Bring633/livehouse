# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LivehouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    category = scrapy.Field()#所属类别
    show_date = scrapy.Field()#演出的日期时间
    city = scrapy.Field()#所在城市
    loc = scrapy.Field()#所在场地
    show_name = scrapy.Field()#场次的名字
    shower = scrapy.Field()#乐队
    state = scrapy.Field()#售票状态
    provider = scrapy.Field()#哪里售卖
    web = scrapy.Field()#网址
    sale_price = scrapy.Field()#价格
    target_shower = scrapy.Field()
    
    pass
