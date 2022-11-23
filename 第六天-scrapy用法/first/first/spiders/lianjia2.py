import scrapy
import json
from ..items import FirstItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia2'

    def start_requests(self):
        for i in range(1, 11):
            url = f'https://hz.fang.lianjia.com/loupan/pg{i}rshangzhou/?_t=1'
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
            }
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

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
