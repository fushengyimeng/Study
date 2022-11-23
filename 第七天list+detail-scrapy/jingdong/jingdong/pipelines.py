
import pymysql


class JingdongPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='123456',database='new_insert')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into jd_data values (%s, %s, %s, %s, %s, %s)'
        data = (0, item['title'], item['sku_id'], item['vender_id'], item['price'], item['origin_price'])
        self.cursor.execute(sql, data)
        self.conn.commit()
        return item

