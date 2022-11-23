import scrapy
import json
import datetime
from ..items import DuodianShopItem
from scrapy_redis.spiders import RedisSpider


class ShopSpider(RedisSpider):
    name = 'shop'
    redis_key = 'gwd'

    def make_request_from_data(self, data):
        data = json.loads(data)
        lng = data.get('lng')
        #get方法，获取值，如果没有则用空值代替
        lat = data.get('lat')
        province = data.get('province')
        city = data.get('city')
        county = data.get('county')
        url = 'https://flow.dmall.com/app/home/business'
        data = {
            'param': '{"deliveryLocation":{"latitude":%s,"longitude":%s,"regionCode":"330105"},"mode":"online","onlineBizCode":1,"onlineShowType":1,"onlineStore":"416","userLocation":{"latitude":30.343558,"longitude":120.120662,"regionCode":"330110"},"wifiList":[{"bssid":"48:0e:ec:90:b6:64","signal":"-46"},{"bssid":"cc:08:fb:f4:fd:b9","signal":"-40"},{"bssid":"48:0e:ec:90:b6:66","signal":"-54"},{"bssid":"cc:08:fb:f4:fd:b7","signal":"-36"}]}' % (lat, lng)}
        headers = {
            'dmTenantId': '1',
            'venderId': '2',
            'User-Agent': 'dmall/5.0.0 Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM1.171019.014)',
            'screen': '2392*1440',
            'deliveryLat': '30.345347',
            'recommend': '1',
            'uuid': '00000000-6d7c-d0a4-b744-b3c10033c587',
            'appMode': 'online',
            'platform': 'ANDROID',
            'utmId': '',
            'firstInstallTime': '1615376466393',
            'deliveryLng': '120.121991',
            'businessCode': '1',
            'apiVersion': '5.0.0',
            'xyz': 'ac',
            'networkType': '1',
            'channelId': 'dm010205000004',
            'lat': '30.344606',
            'oaid': '',
            'androidId': 'e1fc6030270ea8a4',
            'storeGroupKey': '804338927e3a3d9a99ff97fb0d28e631@MS00MTYtMg',
            'sysVersion': 'Android-8.1.0',
            'utmSource': '',
            'platformStoreGroupKey': '583ddc34cedd821fbaefe94cece0b027@MjA3LTE3NjIx',
            'lng': '120.121128',
            'appName': 'com.wm.dmall',
            'tpc': '',
            'isOpenNotification': '1',
            'wifiState': '1',
            'sessionId': 'bacb9272a51f4a10815a89050c8e853f',
            'storeId': '416',
            'env': 'app',
            'userId': '',
            'version': '5.0.0',
            'token': '',
            'currentTime': '1615376681459',
            'lastInstallTime': '1615376466393',
            'tdc': '',
            'areaId': '330110',
            'gatewayCache': '',
            'risk': '1',
            'originBusinessFormat': '1-4-8',
            'dSource': '',
            'device': 'Google google Pixel XL OPM1.171019.014',
            'ticketName': '',
            'smartLoading': '1',
            'cid': '',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Content-Length': '368',
            'Host': 'flow.dmall.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        meta = {
            'lng': lng,
            'lat': lat,
            'province': province,
            'city': city,
            'county': county
        }
        return scrapy.FormRequest(url=url, formdata=data, headers=headers, meta=meta, callback=self.parse)

    def parse(self, response):
        item = DuodianShopItem()
        json_data = json.loads(response.text)
        data_list1 = json_data['data']['online']['storeList']
        if data_list1:
            for data_list in data_list1:
                item['storeId'] = str(data_list['storeId'])
                if data_list['storeId'] == 999999:
                    pass
                else:
                    item['storeName'] = data_list['storeName']
                    item['venderId'] = str(data_list['venderId'])
                    item['venderName'] = data_list['venderName']
                    item['storeAddress'] = data_list.get('storeAddress', '')
                    item['province'] = response.meta['province']
                    item['city'] = response.meta['city']
                    item['county'] = response.meta['county']
                    item['longitude'] = str(data_list.get('longitude', ''))
                    item['latitude'] = str(data_list.get('latitude', ''))
                    item['update_time'] = str(datetime.datetime.now())
                    yield item
        else:
            print('该经纬度下没有店铺..')


