import requests
import json



url = 'http://shop.kongfz.com/ranklist/?event=all&currPage=5&async=1&_=1620800412314'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
resp = requests.get(url,headers=headers)
str_data = json.loads(resp.text)
data = str_data['result']['list']
print(data)