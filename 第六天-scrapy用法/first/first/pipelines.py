import pymysql


class FirstPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='123456',database='new_insert')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into lianjia_data values (%s, %s, %s,  %s, %s, %s, %s, %s, %s)'
        data = (0, item['name'], item['district_name'], item['bizcircle_name'], item['address'], item['frame_rooms_desc'], item['resblock_frame_area'], item['reference_total_price'], item['reference_total_price_unit'])
        self.cursor.execute(sql, data)
        self.conn.commit()
        print('插入成功')
        return item
