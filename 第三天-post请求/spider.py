import requests

cookies = {
    'OUTFOX_SEARCH_USER_ID': '-1528107425@10.168.8.63',
    'OUTFOX_SEARCH_USER_ID_NCOO': '1286367575.2578924',
    'JSESSIONID': 'abcaSQQp32tu2bUsQI9Fx',
    'DICT_UGC': 'be3af0da19b5c5e6aa4e17bd8d90b28a|',
    '_ntes_nnid': '6eb8abc128f959f8c2d11101d517e014,1614866485842',
    '___rl__test__cookies': '1614866524756',
}

headers = {
    'Origin': 'http://fanyi.youdao.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://fanyi.youdao.com/?http://home.cnblogs.com/u/936075/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = (
    ('smartresult', ['dict', 'rule']),
)

data = {
  'i': '\u4E2D\u56FD',
  'from': 'AUTO',
  'to': 'AUTO',
  'smartresult': 'dict',
  'client': 'fanyideskweb',
  'salt': '16148665247582',
  'sign': '595051a446a9ff2935171e5412b16e04',
  'lts': '1614866524758',
  'bv': '7e3150ecbdf9de52dc355751b074cf60',
  'doctype': 'json',
  'version': '2.1',
  'keyfrom': 'fanyi.web',
  'action': 'FY_BY_CLICKBUTTION'
}

response = requests.post('http://fanyi.youdao.com/translate_o', headers=headers, params=params, cookies=cookies, data=data, verify=False)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule', headers=headers, cookies=cookies, data=data, verify=False)
