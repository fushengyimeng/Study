import redis
import json


class SaveData:
    def __init__(self):
        self.r = redis.Redis(host='localhost',port=6379,db=3)

    def set_data_to_redis(self):
        self.r.lpush('key', json.dumps({'name': 'hx'}))
        print('插入成功')

    def get_data_from_redis(self):
        result = self.r.lrange('key',0, 2)
        print(result)

    def main(self):
        self.get_data_from_redis()


if __name__ == '__main__':
    spider = SaveData()
    spider.main()