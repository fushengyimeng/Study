import pymysql


class Spider:

    def __init__(self):
        self.conn, self.cursor = self.conn_mysql()

    def conn_mysql(self):
        conn = pymysql.connect(host='localhost', user='root',password='123456',database='new_insert')
        cursor = conn.cursor()  # 得到一个可以执行SQL语句的光标对象
        print('连接成功......')
        return conn, cursor

    # 查询
    def select_sql(self):
        sql = 'select * from name'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(result)

    # 插入
    def insert_into(self):
        # 第一种写法
        # sql = 'insert into name(id, name) value (2, "wsk")'
        # 第二种写法
        sql = 'insert into name values (0, "bbb")'
        self.cursor.execute(sql)
        self.conn.commit()
        print('插入成功...')

    # 更新
    def update_sql(self):
        sql = 'update name set name = "ddd" where id = 2'
        self.cursor.execute(sql)
        self.conn.commit()
        print('更新成功')

    # 删除
    def delete_sql(self):
        sql = 'delete from name where id = 1'
        self.cursor.execute(sql)
        self.conn.commit()
        print('删除成功')

    def main(self):
        self.delete_sql()

if __name__ == '__main__':
    spider = Spider()
    spider.main()