import json
import asyncio
import aiohttp
import time
# import pymysql
from lxml import etree


class Spider:
    def __init__(self, loop=None):
        self.loop = loop
        # self.conn, self.cursor = self.mysql_con()
        self.xz_bf = asyncio.Semaphore(5)

    # def mysql_con(self):
    #     conn = pymysql.connect()
    #     cursor = conn.cursor()
    #     return conn, cursor

    # async def save_data(self, sql):
    #     self.cursor.execute(sql)
    #     self.conn.commit()

    async def get_list(self, page):
        times = str(time.time() * 1000).split('.')[0]
        url = 'http://shop.kongfz.com/ranklist/?event=all&currPage={}&async=1&_={}'.format(page, times)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                str_data = await resp.text()
                json_data = json.loads(str_data)
                data_list = json_data['result']['list']
                await asyncio.gather(*[self.xz_detail(single_data['shopId'], single_data['userId']) for single_data in data_list])

    async def xz_detail(self, shop_id, user_id):
        async with self.xz_bf:
            await self.get_detail(shop_id, user_id)

    async def get_detail(self, shop_id, user_id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
        }
        detail_url = f'http://shop.kongfz.com/widget/ajax?widget=shopInfo&tpl=store&api=getShopInfo&shopId={shop_id}&userId={user_id}&_={str(time.time() * 1000).split(".")[0]}'
        async with aiohttp.ClientSession() as session:
            async with session.get(detail_url, headers=headers) as resp:
                str_data = await resp.text()
                print('detail_data =>', str_data)
                # sql = 'insert into table_name values()'
                # await self.save_data(sql)

    async def start(self):
        await asyncio.gather(*[self.get_list(page) for page in range(1, 2)])

    async def main(self):
        await self.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    spider = Spider(loop)
    loop.run_until_complete(spider.main())
