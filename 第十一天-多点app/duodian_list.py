import requests
import pymysql


class Spider:
    def __init__(self):
        self.conn,self.cursor = self.parse()
        self.id = '12440'
    def select_data(self):
        sql1 = 'select storeId,venderId from duodian'
        self.cursor.execute(sql1)
        a = self.cursor.fetchall()
        for info in a:
            storeid = info[0]
            venderid = info[1]
            self.get(storeid,venderid)




    def get(self,a,b):
        url = 'https://searchgw.dmall.com/app/new/wareCategory/list'
        headers ={
            'User-Agent': 'dmall/4.8.4 Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM1.171019.014)',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'searchgw.dmall.com',
        }

        data = 'param={"from":1,"queryType":0,"storeInfo":{"businessCode":99,"defaultChosed":false,"name":"","storeId":"%s","timestamp":"","venderId":"%s"}}'%(a,b)
        html = requests.post(url,headers = headers,data = data).text
        print(html)

        # app_data = html['data']['wareCategory']
        # print(app_data)
        # for data in app_data:
        #     list = data['categoryList']
        #     for info in list:
        #         categoryId = info['categoryId']
        #         categoryName = info['categoryName']
        #         categoryType = info['categoryType']
        #         childCategoryList = info.get('childCategoryList','')
        #         print(categoryId,categoryName)
        #         if childCategoryList:
        #             for childlist in childCategoryList:
        #                 cId = childlist['categoryId']
        #                 cName = childlist['categoryName']
        #                 cType = childlist['categoryType']
        #                 print(cId,cName)
        #                 sql = f'insert into duodian_category values("{self.id}","{categoryId}","{categoryName}","{categoryType}","{cId}","{cName}","{cType}")'
        #                 self.insert_mysql(sql)
        #         else:
        #             sql = f'insert into duodian_category values("{self.id}","{categoryId}","{categoryName}","{categoryType}"," "," "," ")'
        #             self.insert_mysql(sql)


    def parse(self):
        conn = pymysql.connect(host = 'localhost', user = 'root',password = '123456',db='new_insert')
        cursor = conn.cursor()
        return conn,cursor

    def insert_mysql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def main(self):
        self.select_data()

if __name__ == '__main__':
    spider = Spider()
    spider.main()