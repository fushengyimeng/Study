import requests


class Proxy:
    def __init__(self):
        pass

    # 静态ip / 免费Ip
    def staic_proxy(self):
        proxies = {
            'http': 'http://113.13.177.75:8888',
            'https': 'http://113.13.177.75:8888'
        }
        return proxies

    # 付费代理Ip 动态转发
    def money_proxy(self):
        # 代理服务器
        proxyHost = "forward.apeyun.com"
        proxyPort = "9082"
        # 代理隧道验证信息
        proxyUser = "2121032700113402018"
        proxyPass = "yQ3uvmx6IBPetHn1"
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }
        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        return proxies

    def use_proxy(self):
        url = 'https://api.ipify.org/?format=json'
        proxies = self.money_proxy()
        # {"ip":"220.191.17.52"} 不加代理返回的本机Ip  加付费代理返回的{"ip":"121.56.37.41"}
        res = requests.get(url, proxies=proxies)
        print('res_proxy =>', res.text)


if __name__ == '__main__':
    spider = Proxy()
    spider.use_proxy()