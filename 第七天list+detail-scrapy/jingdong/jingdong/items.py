
import scrapy


class JingdongItem(scrapy.Item):
    title = scrapy.Field()
    sku_id = scrapy.Field()
    vender_id = scrapy.Field()
    price = scrapy.Field()
    origin_price = scrapy.Field()

