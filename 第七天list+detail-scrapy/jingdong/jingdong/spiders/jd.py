import scrapy
import json
import re
import random
from urllib.parse import urlencode
from lxml import etree
from ..items import JingdongItem


class JdSpider(scrapy.Spider):
    name = 'jd'

    def deal_res(self, a):
        pattern = re.compile('.*?\((.*)\)')
        result = pattern.findall(a)
        json_data = json.loads(result[0])
        return json_data

    def start_requests(self):
        for i in range(1, 5):
            print(i)
            headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cookie': 'shshshfpa=79ef86cd-9263-a905-67b0-c6f1968af4a9-1556530958; shshshfpb=hX4B6HkwMoYHPS76whNIHDA%3D%3D; __jdu=1123382582; areaId=15; ipLoc-djd=15-1213-1214-0; PCSYCityID=CN_330000_330100_330110; unpl=V2_ZzNtbUJSQRxwDBVdehELVWIBEg1LURQVIAhFXS5NWVY3CxRUclRCFnUUR1ZnGFUUZwsZX0BcRxVFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsZXwdlChFZS1RzJXI4dmR4GVUDbwciXHJWc1chVERcfhxbSGcDEV9AXkARfAt2VUsa; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_143845b809fa431a87f1d128de4ba978|1615203231762; shshshfp=f4afbe2aefc7e00f34e29d20f7cb2105; __jda=122270672.1123382582.1615183221.1615183222.1615203232.2; __jdc=122270672; qrsc=1; rkv=1.0; 3AB9D23F7A4B3C9B=FYLF47UK23PA25IDQAQUD4IT4JGNJYGFKMGOERMSI3GWVNEJQE75HKY2N6TXX7KLOUXYIRA72WTC7YIWHEU2FVGG5Q; shshshsID=785b9420ffb8f221fa8f0e8312328b3d_7_1615203693087; __jdb=122270672.7.1123382582|2.1615203232',
                'referer': 'https://search.jd.com/Search?keyword=python&wq=python&page=1&s=1&click=0',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
            }
            params = {
                'keyword': 'python',
                'wq': 'python',
                'page': f'{i}',
                's': '1',
                'click': '0'
            }
            url = f'https://search.jd.com/s_new.php?{urlencode(params)}'
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        xpath_data = etree.HTML(response.text)
        data_list = xpath_data.xpath('//ul[@class="gl-warp clearfix"]/li')
        print(len(data_list))
        for data in data_list:
            sku_id = data.xpath('./@data-sku')[0]
            vender_id = data.xpath('.//div[@class="p-img"]/div/@data-venid')[0]
            title = ''.join(data.xpath('.//div[@class="p-name"]/a/em//text()'))
            meta = {
                'sku_id': sku_id,
                'vender_id': vender_id,
                'title': title,
            }
            url = f'https://item.jd.com/{sku_id}.html'
            headers = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
            }
            yield scrapy.Request(url, headers=headers, meta=meta, callback=self.get_detail1)

    def get_detail1(self, response):
        pattern = re.compile('cat: \[(.*?)\]')
        result = pattern.findall(response.text)[0]
        params = {
            'skuId': f'{response.meta["sku_id"]}',
            'cat': f'{result}',
            'venderId': f'{response.meta["vender_id"]}',
            'area': '15_1213_1214_0',
            'buyNum': '1',
            'choseSuitSkuIds': '',
            'extraParam': '{"originid":"1"}',
            'ch': '1',
            'fqsp': '0',
            'pduid': '1123382582',
            'pdpin': '',
            'coord': '',
            'detailedAdd': '',
            'callback': 'jQuery9199410'
        }
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': 'https://item.jd.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        meta = response.meta
        url = f'https://c0.3.cn/stock?{urlencode(params)}'
        yield scrapy.Request(url, headers=headers, meta=meta, callback=self.get_detail)


    def get_detail(self, response):
        item = JingdongItem()
        try:
            json_data = self.deal_res(response.text)
            item['title'] = response.meta['title']
            item['sku_id'] = response.meta['sku_id']
            item['vender_id'] = response.meta['vender_id']
            item['price'] = json_data['stock']['jdPrice']['p']
            item['origin_price'] = json_data['stock']['jdPrice']['m']
            yield item

        except Exception as e:
            print(e)
            print(response.meta['sku_id'])






