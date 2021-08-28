# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BuffItem(scrapy.Item):
    # define the fields for your item here like:
    goods_id = scrapy.Field()
    goods_name = scrapy.Field()
    steam_price_cny = scrapy.Field()
    steam_price = scrapy.Field()
    buff_price = scrapy.Field()
    pass
