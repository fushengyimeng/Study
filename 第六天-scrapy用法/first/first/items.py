import scrapy


class FirstItem(scrapy.Item):
    name = scrapy.Field()
    district_name = scrapy.Field()
    bizcircle_name = scrapy.Field()
    address = scrapy.Field()
    frame_rooms_desc = scrapy.Field()
    resblock_frame_area = scrapy.Field()
    reference_total_price = scrapy.Field()
    reference_total_price_unit = scrapy.Field()
