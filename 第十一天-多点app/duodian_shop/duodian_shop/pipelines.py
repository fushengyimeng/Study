import pymysql


class DuodianShopPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='123456',database='new_insert')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert ignore into duodian values (%s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s)'
        data = (item['storeId'], item['storeName'], item['venderId'], item['venderName'], item['storeAddress'], item['province'], item['city'], item['county'], item['longitude'], item['latitude'], item['update_time'])
        self.cursor.execute(sql, data)
        self.conn.commit()
        print('插入成功')
        return item