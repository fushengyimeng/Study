import scrapy


class DuodianShopItem(scrapy.Item):
    storeId = scrapy.Field()
    storeName = scrapy.Field()
    venderId = scrapy.Field()
    venderName = scrapy.Field()
    storeAddress = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    update_time = scrapy.Field()

