import requests
import time
import random
from hashlib import md5


class Spider:
    def __init__(self):
        pass

    def encrypt_md5(self, s):
        new_md5 = md5()
        new_md5.update(s.encode(encoding='utf-8'))
        return new_md5.hexdigest()

    def start(self, content):
        cookies = {
            'OUTFOX_SEARCH_USER_ID': '-1528107425@10.168.8.63',
            'OUTFOX_SEARCH_USER_ID_NCOO': '1286367575.2578924',
            '_ntes_nnid': '6eb8abc128f959f8c2d11101d517e014,1614866485842',
            'JSESSIONID': 'aaa4B5Q3oKRpZ7EnnUwGx',
            '___rl__test__cookies': '1615288931083',
        }
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        params = (
            ('smartresult', ['dict', 'rule']),
        )
        lts = str(time.time() * 1000).split('.')[0]
        salt = lts + f'{random.randint(0, 10)}'
        need_encrypt_string = 'fanyideskweb' + content + salt + 'Tbh5E8=q6U3EXe+&L[4c@'
        sign = self.encrypt_md5(need_encrypt_string)
        print('sign =>', sign)
        data = {
            # 搜索的关键字
            'i': f'{content}',
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,  # 动态的
            'sign': sign,  # 动态的
            'lts': lts,  # 动态的
            'bv': '51c157d16589f89e7109f585b4553d23',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'
        }
        response = requests.post('http://fanyi.youdao.com/translate_o', headers=headers, params=params, cookies=cookies, data=data, verify=False)
        print(response.text)

    def main(self):
        self.start('中国')


if __name__ == '__main__':
    spider = Spider()
    spider.main()
