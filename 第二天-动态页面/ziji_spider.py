import requests
import json
from urllib.parse import urlencode


class Spider:
    def __init__(self):
        pass

    def get_data(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Connection': 'keep-alive',
            'Cookie': 'acw_tc=2760820616147815550961330ee3272e97f4f99648c2b5340e380b17bd6bf9; xq_a_token=62effc1d6e7ddef281d52c4ea32f6800ce2c7473; xqat=62effc1d6e7ddef281d52c4ea32f6800ce2c7473; xq_r_token=53a0f79d5bae795fb7abc6814dc0fc0410413016; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxNTYwMzIxNSwiY3RtIjoxNjE0NzgxNDk5MTA4LCJjaWQiOiJkOWQwbjRBWnVwIn0.P1vQQSxkYODPoZ7NmxOlncTMf15dqEu4x04hqSfdUJWau20k98d_aQUjcLumZQWtQ1qQGHrjLX4Mw9K-3xya8z_y2etZBEAVcL_OmCmYEslaNnePkwot_fZ-fpfRWaGKv5VcQAQkn-_0NKcWd2P6tEdsuq4oZAB2WfrLLWsyVDvTQluzOwEPWsMZfAd7DeWGPehuElGN75ez05xekPCOTqCojRTHdga-aZsD9IS2Bqh2KDOUrp8rWUtibf7-KjQkHSY-jPh_8gLnYEMDx87WexRENJQ--aYFkrPKYcMFFZmxts7lr4wAtVQtKpsFESHYiFD28s_4iRJVU0XbN5AanA; u=511614781555101; Hm_lvt_1db88642e346389874251b5a1eded6e3=1614781557; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1614781892',
            # 'elastic-apm-traceparent': '00-3365a2c59ce889761de02e3fef8bc06f-08296beef281025e-01',
            'Host': 'xueqiu.com',
            'Referer': 'https://xueqiu.com/',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        params = {
            'since_id': '-1',
            'max_id': '176439',
            'size': '15'
        }
        url = f'https://xueqiu.com/statuses/hot/listV2.json?{urlencode(params)}'
        res = requests.get(url, headers=headers).text
        print(res)
        
        json_data = json.loads(res)
        data_list = json_data['items']
        print(data_list)
        for single_data in data_list:
            title = single_data['original_status']['title']
            description = single_data['original_status']['description']
            print(title)
            print(description)

    def main(self):
        self.get_data()


if __name__ == '__main__':
    spider = Spider()
    spider.main()