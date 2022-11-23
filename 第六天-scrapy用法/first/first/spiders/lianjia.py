import scrapy
import json
from ..items import FirstItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    start_urls = ['https://hz.fang.lianjia.com/loupan/pg2rshangzhou/?_t=1']


    def parse(self, response):
        json_data = json.loads(response.text)
        data_list = json_data['data']['list']
        item = FirstItem()
        for single_data in data_list:
            item['name'] = single_data['resblock_name']
            item['district_name'] = single_data['district_name']
            item['bizcircle_name'] = single_data['bizcircle_name']
            item['address'] = single_data['address']
            item['frame_rooms_desc'] = single_data['frame_rooms_desc']
            item['resblock_frame_area'] = single_data['resblock_frame_area']
            item['reference_total_price'] = single_data['reference_total_price']
            item['reference_total_price_unit'] = single_data['reference_total_price_unit']
            yield item


