import redis
import pymysql
import json
import threading
import queue
import datetime

r = redis.Redis('localhost', port=6379, db=15)


class PushData(threading.Thread):
    def __init__(self, q=None):
        threading.Thread.__init__(self)
        self.lat = ''
        self.lng = ''
        self.q = q

    def run(self) -> None:
        self.deal_request_data()

    def get_gwd_data(self):
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='new_insert'
        )
        cursor = conn.cursor()
        sql = 'select * from location'
        cursor.execute(sql)
        data_list = cursor.fetchall()
        return data_list

    def push_start_url_data(self, request_data):
        r.lpush('gwd', json.dumps(request_data))
        r.close()

    def deal_request_data(self):
        lng, lat, province, city, county = self.q.get().split('-')
        request_data = {
            'lng': lng,
            'lat': lat,
            'province': province,
            'city': city,
            'county': county
        }
        try:
            self.push_start_url_data(request_data)
        except Exception as e:
            pass


def main():
    q = queue.Queue()
    spider = PushData(q)
    gwd_list = spider.get_gwd_data()
    for gwd_data in gwd_list:
        lng = list(gwd_data)[3]
        lat = list(gwd_data)[4]
        province = list(gwd_data)[0]
        city = list(gwd_data)[1]
        county = list(gwd_data)[2]
        q.put(f'{lng}-{lat}-{province}-{city}-{county}')

    while not q.empty():
        threading_list = []
        for count in range(50):
            spider = PushData(q)
            threading_list.append(spider)
        for t in threading_list:
            t.start()
        for t in threading_list:
            t.join()


if __name__ == '__main__':
    print(datetime.datetime.now())
    main()
    print(datetime.datetime.now())
