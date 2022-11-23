import json
import requests


def get_data(page=None):
    headers = {
        'venderId': '2',
        'User-Agent': 'dmall/4.8.4 Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM1.171019.014)',
        'screen': '2392*1440',
        'deliveryLat': '30.345347',
        'recommend': '1',
        'uuid': '00000000-6d7c-d0a4-b744-b3c10033c587',
        'appMode': 'online',
        'platform': 'ANDROID',
        'utmId': '',
        'firstInstallTime': '1615382576972',
        'deliveryLng': '120.121991',
        'businessCode': '8352',
        'apiVersion': '4.8.4',
        'xyz': 'ac',
        'networkType': '1',
        'channelId': 'dm010205000004',
        'lat': '30.344643',
        'oaid': '',
        'androidId': 'e1fc6030270ea8a4',
        'storeGroupKey': '804338927e3a3d9a99ff97fb0d28e631@MS00MTYtMg',
        'sysVersion': '8.1.0',
        'utmSource': '',
        'platformStoreGroupKey': '141cc1750f60df3179b77e6e0d23d517@MjA3LTE3NjIx',
        'lng': '120.121321',
        'appName': 'com.wm.dmall',
        'tpc': 'category_66106',
        'isOpenNotification': '1',
        'wifiState': '1',
        'sessionId': '1fbbf3c9d3f34c9c9fa56d0334d81b39',
        'storeId': '416',
        'env': 'app',
        'userId': '',
        'version': '4.8.4',
        'token': '',
        'storeGroupV4': '',
        'currentTime': '1615555200027',
        'lastInstallTime': '1615382576972',
        'tdc': '',
        'areaId': '330110',
        'gatewayCache': '',
        'platformStoreGroup': '',
        'dSource': '',
        'device': 'google Pixel XL OPM1.171019.014',
        'ticketName': '',
        'smartLoading': '1',
        'cid': '13065ffa4ea1bf6f089',
        'dnsSdkVersion': '1.0.0',
        'appVersion': '4.8.4',
        'ISPCode': '',
        'platformType': 'ANDROID',
        'appCode': '0',
        'netStatus': 'wifi',
        'deviceName': 'Pixel XL',
        'manufacturer': 'Google',
        'Host': 'searchgw.dmall.com',
    }
    if page:
        page_number = page
    else:
        page_number = 1
    print(f'当前请求的页码为= >{page_number}')
    data = {
        'param': '{"brandId":"","categoryId":"66106","categoryLevel":2,"categoryType":1,"from":1,"noResultSearch":0,"pos":1,"queryType":0,"selectOption":[{"checked":true,"childPropertyId":"66107","propertyId":"2"}],"sortKey":0,"sortRule":0,"src":0,"storeInfo":{"businessCode":99,"defaultChosed":false,"name":"","storeId":"416","timestamp":"","venderId":"2"},"pageNum":"%s","pageSize":"20"}' % (
            page_number)
    }

    response = requests.post('https://searchgw.dmall.com/app/new/search/wareSearch', headers=headers, data=data).json()
    data_list = response['data']['wareList']
    all_pages = response['data']['pageInfo']['pageCount']
    for data in data_list:
        title = data['wareName']
        price = int(data['warePrice']) / 100
        print(title)
        print(price)
    if page_number == all_pages:
        pass
    else:
        page_number += 1
        get_data(page_number)



get_data()

