# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FactoryspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    login_money = scrapy.Field()
    order_type = scrapy.Field()
    scale = scrapy.Field()
    main_category = scrapy.Field()
    type = scrapy.Field()
    product_level = scrapy.Field()
    produce_time = scrapy.Field()
    img = scrapy.Field()
    pass
