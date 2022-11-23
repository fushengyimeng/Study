import time
import datetime
import asyncio


class Spider:
    def __init__(self, loop=None):
        self.loop = loop

    async def b(self, i):
        print(i)

    async def main(self):
        await asyncio.gather(*[self.b(i) for i in range(1, 101)])



if __name__ == '__main__':
    print(datetime.datetime.now())
    loop = asyncio.get_event_loop()
    spider = Spider(loop)
    loop.run_until_complete(spider.main())
    print(datetime.datetime.now())
