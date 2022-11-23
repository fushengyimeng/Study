import requests
import json
import pymysql
import datetime

class Spider:
    def __init__(self):
        self.conn,self.cursor = self.conn()

    def start(self):
        url = 'https://flow.dmall.com/app/home/business'
        data = 'param={"deliveryLocation":{"latitude":31.037852,"longitude":121.640481,"regionCode":"330105"},"mode":"online","onlineBizCode":1,"onlineShowType":1,"onlineStore":"416","userLocation":{"latitude":30.343558,"longitude":120.120662,"regionCode":"330110"},"wifiList":[{"bssid":"48:0e:ec:90:b6:64","signal":"-46"},{"bssid":"cc:08:fb:f4:fd:b9","signal":"-40"},{"bssid":"48:0e:ec:90:b6:66","signal":"-54"},{"bssid":"cc:08:fb:f4:fd:b7","signal":"-36"}]}'
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
            'utmId':'',
            'firstInstallTime': '1615376466393',
            'deliveryLng': '120.121991',
            'businessCode': '1',
            'apiVersion': '5.0.0',
            'xyz': 'ac',
            'networkType': '1',
            'channelId': 'dm010205000004',
            'lat': '30.344606',
            'oaid':'',
            'androidId': 'e1fc6030270ea8a4',
            'storeGroupKey': '804338927e3a3d9a99ff97fb0d28e631@MS00MTYtMg',
            'sysVersion': 'Android-8.1.0',
            'utmSource':'',
            'platformStoreGroupKey': '583ddc34cedd821fbaefe94cece0b027@MjA3LTE3NjIx',
            'lng': '120.121128',
            'appName': 'com.wm.dmall',
            'tpc':'',
            'isOpenNotification': '1',
            'wifiState': '1',
            'sessionId': 'bacb9272a51f4a10815a89050c8e853f',
            'storeId': '416',
            'env': 'app',
            'userId':'',
            'version': '5.0.0',
            'token':'',
            'currentTime': '1615376681459',
            'lastInstallTime': '1615376466393',
            'tdc':'',
            'areaId': '330110',
            'gatewayCache':'',
            'risk': '1',
            'originBusinessFormat': '1-4-8',
            'dSource':'',
            'device': 'Google google Pixel XL OPM1.171019.014',
            'ticketName':'',
            'smartLoading': '1',
            'cid':'',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '368',
            'Host': 'flow.dmall.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        res = requests.post(url, headers=headers, data=data)
        print(res.text)
        exit()
        duodian_data = res.json()['data']['offline']['storeList']
        for data in duodian_data:
            print(data)
            storeId = data['storeId']
            storeName = data['storeName']
            venderName = data.get('venderName', '')
            storeAddress = data['storeAddress']
            longitude = data['longitude']
            latitude = data['latitude']
            self.sql_data(storeId, storeName, venderName, storeAddress, longitude, latitude)
        # return storeId, storeName, venderName, storeAddress, longitude, latitude

    def conn(self):
        conn = pymysql.connect(host = 'localhost',user = 'root',password = '123456',database = 'new_insert')
        cursor = conn.cursor()
        return conn,cursor

    def sql_data(self,a, b, c, d, e, f):
        sql = f'insert ignore into duodian values("{a}","{b}","{c}","{d}","{e}","{f}","{datetime.datetime.now()}")'
        self.cursor.execute(sql)
        self.conn.commit()

    def main(self):
        self.start()


if __name__ == '__main__':
    spider = Spider()
    spider.main()