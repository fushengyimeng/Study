import requests
from urllib.parse import urlencode

params = {
    'lng':"114.804372",
    "method":"ddsy.user.query.address.locationInfo",
    "t":"2021-03-15 19:38:17",
    "v":"1.0",
    "sign":"AE0E2D7FF018DDD76379F83BDD6F87BE",
    "lat":"22.648243"
}
url = f"https://api.ddky.com/user/rest.htm?{urlencode(params)}"
headers = {
        'X-Tingyun-Id':'p35OnrDoP8k;c=2;r=1871795121;',
        'Connection':'close',
        # Charset	utf-8
        # http.agent	com.ddsy (Android 8.1.0; Pixel XL Build/OPM1.171019.014)
        # Accept-Encoding	gzip,deflate
        # screenWidth	1440
        # lng
        # city
        # macid	02%3A00%3A00%3A00%3A00%3A00
        # screenHeight	2392
        # loginToken
        # language	zh
        # imsi	NaN
        # versionName	5.8.0
        # platform	android8.1.0
        # uid
        # imei0	352693081755791
        # uDate
        # imei	AndroidID72884a4822e84d2d
        # model	Pixel+XL
        # channelName	alisd
        # lat
        'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM1.171019.014)',
        'Host':'api.ddky.com'
}
html = requests.get(url,headers=headers)
print(html.text)
shops = html.json()['data']['shops']
for shop in shops:
    companyId = shop['companyId']
    shopName = shop['shopName']
    shopId = shop['shopId']
    print(shopName,shopId)


