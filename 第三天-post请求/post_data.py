import requests
from urllib.parse import urlencode

class Spider:
    def __init__(self):
        pass

    def get_data(self):
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '252',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/?http://home.cnblogs.com/u/936075/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1528107425@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=1286367575.2578924; JSESSIONID=abcaSQQp32tu2bUsQI9Fx; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; _ntes_nnid=6eb8abc128f959f8c2d11101d517e014,1614866485842; ___rl__test__cookies=1614867921997',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        params = {
            'smartresult': 'dict',
            'smartresult': 'rule'
        }
        url = f'http://fanyi.youdao.com/translate_o?{urlencode(params)}'
        print(url)
        data = {
            'i': '中国',
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '16148679220067',
            'sign': '2f059b405ec4a356defe559ac2b88f91',
            'lts': '1614867922006',
            'bv': '7e3150ecbdf9de52dc355751b074cf60',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        res = requests.post(url, data=data, headers=headers)
        print(res.text)

    def main(self):
        self.get_data()

if __name__ == '__main__':
    spider = Spider()
    spider.main()




