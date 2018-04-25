# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class YiseeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()#小说名
    author = Field()#作者名
    type = Field()#小说分类
    zhangjie =Field()
    content =Field()

# class YiSeeZJ(scrapy.Item):
#     zhangjie = Field()  # 小说章节名
#     content = Field()  # 对应的章节内容