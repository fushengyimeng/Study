import time
import datetime
import asyncio


class Spider:
     def a(self):
        time.sleep(2)

     def b(self):
        for i in range(1, 1000000):
            if i % 100000 == 0:
                print(i)


if __name__ == '__main__':
    spider = Spider()
    print(datetime.datetime.now())
    spider.b()
    print(datetime.datetime.now())