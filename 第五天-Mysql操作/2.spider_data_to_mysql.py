import pymysql
import requests
from lxml import etree

class Spider:
    def __init__(self):
        self.conn,self.cursor = self.conn_sql()


    def get_html(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_abcde_qweasd=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=SIr7mzLGEVOeoJfcQvDpQBZBIWH1FmreHGsOMkx0OuK&wd=&eqid=9f523d3000001acd0000000460423ab5; _abcde_qweasd=0; Hm_lvt_5ef477151c16f262c2b8453ff605b37f=1614953147; bdshare_firstime=1614953146666; Hm_lpvt_5ef477151c16f262c2b8453ff605b37f=1614953154',
            'Host': 'www.paoshuzw.com',
            'Referer': 'http://www.paoshuzw.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }
        url = 'http://www.paoshuzw.com/paihangbang/'
        return headers,url

    def parsh_data(self):
        headers,url = self.get_html()
        html = requests.get(url=url,headers=headers).text
        tree = etree.HTML(html)
        data = tree.xpath('//*[@id="main"]/div[2]/ul[1]/li[2]//text()')[1]
        print(data)
        sql = f'insert into name values(0,"{data}")'
        self.cursor.execute(sql)
        self.conn.commit()
        print("/////////////")
    def conn_sql(self):
        conn = pymysql.connect(host="localhost",user='root',password='123456',database='new_insert')
        cursor = conn.cursor()
        return conn,cursor


    def main(self):
        self.parsh_data()

if  __name__ == '__main__':
    spider = Spider()
    spider.main()