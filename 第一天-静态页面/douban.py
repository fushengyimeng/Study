import requests

cookies = {
    'gr_user_id': '1f09b750-50e3-4df5-8bcc-efbeba0bf0fb',
    'douban-profile-remind': '1',
    '__utmv': '30149280.16867',
    'douban-fav-remind': '1',
    'll': '118172',
    'bid': 'hDW2rmTk4wg',
    '__gads': 'ID=f25f309d99a1e232-224fd6b936c600a8:T=1614781525:RT=1614781525:S=ALNI_MbX6-OnS3XDI9K3GEPk_isjdZWJPQ',
    '__utma': '30149280.235878021.1555062622.1614781444.1618222448.12',
    '__utmc': '30149280',
    '__utmz': '30149280.1618222448.12.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '__utmt': '1',
    'ap_v': '0,6.0',
    '_vwo_uuid_v2': 'D0A6A92B99D12278B18DA44EAED152710|25fa455a90fb8efddb671c07dda494f6',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': '7470fcc8-55fc-46e2-bc45-ca5de56e4c85',
    'gr_cs1_7470fcc8-55fc-46e2-bc45-ca5de56e4c85': 'user_id%3A0',
    '__utmt_douban': '1',
    '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1618222455%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_ses.100001.3ac3': '*',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_7470fcc8-55fc-46e2-bc45-ca5de56e4c85': 'true',
    '__yadk_uid': 'yKUICeUvE9pc24K2mP2N8HFSZjon9dLc',
    '__utmb': '30149280.4.10.1618222448',
    '_pk_id.100001.3ac3': 'bb5978f807474271.1555062622.5.1618222644.1557314274.',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.douban.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

response = requests.get('https://book.douban.com/', headers=headers, cookies=cookies)
print(response.text)