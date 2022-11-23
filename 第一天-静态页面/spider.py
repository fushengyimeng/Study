import requests
from lxml import etree


class Spider:
    def __init__(self):
        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'none',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.cookies = {
            'BIDUPSID': '2BE5AAB2DD1380F417A36F358F907D4A',
            'PSTM': '1544859116',
            'BAIDUID': 'C7F2E3B6DAFCFD23D8E3590BA46A8395:FG=1',
            'BDUSS': 'mF5TEN4QUxvaXdsM05TbUZBcXUwd2Z0TkZTLWUtVldWUWNjbTdnZ1kwYU1oeVZmSVFBQUFBJCQAAAAAAAAAAAEAAAA90bmiaG9tZbrasLXAtMHZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIz6~V6M-v1ea',
            'BDUSS_BFESS': 'mF5TEN4QUxvaXdsM05TbUZBcXUwd2Z0TkZTLWUtVldWUWNjbTdnZ1kwYU1oeVZmSVFBQUFBJCQAAAAAAAAAAAEAAAA90bmiaG9tZbrasLXAtMHZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIz6~V6M-v1ea',
            'BD_UPN': '12314753',
            'H_PS_PSSID': '33273_31254_33594_26350_33265',
            'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
            'BAIDUID_BFESS': 'C7F2E3B6DAFCFD23D8E3590BA46A8395:FG=1',
            'BD_HOME': '1',
            'sugstore': '1',
            '__yjs_duid': '1_a210f9977451e1ffd7091fc89da6ac421614777523829',
            'ab_sr': '1.0.0_NjJkNjNiZjI5YmZhOWFlZTRhNTdiZDE0ODJmYmRmZjBmYjhkOGQzMzc2MGFhNzI4MDYwOGZjMTY1Nzc5NDU0NDMwYmU2M2NmM2M2NmNkYWNlMGU5NWZhMWI3ZDFmMDE1',
            'delPer': '0',
            'BD_CK_SAM': '1',
            'PSINO': '5',
            'H_PS_645EC': '478aIqTu9R0WESmUGgFc0uX24BA1rOpWsO6je8BzESQZHkPE0DcxHQB8othjJcBToi%2B8',
            'BA_HECTOR': '2h80al0k0l8k0g8hdr1g3v38p0q',
            'BDSVRTM': '172',
        }
        self.params = (
            ('ie', 'utf-8'),
            ('f', '8'),
            ('rsv_bp', '1'),
            ('rsv_idx', '2'),
            ('tn', 'baiduhome_pg'),
            ('wd', '\u554A'),
            ('rsv_spt', '1'),
            ('oq', '%E5%95%8A'),
            ('rsv_pq', 'e93ddbfa001f3dfc'),
            ('rsv_t', '9a66NAvP//ME7J8jjjxs2TCiNC1DJE8nNpL8LIBwnDcmsMIR6XX6+CGSY6fmKjb9I2tU'),
            ('rqlang', 'cn'),
            ('rsv_enter', '0'),
            ('rsv_dl', 'tb'),
            ('rsv_btype', 't'),
        )

    def _xpath(self):
        url = 'https://www.baidu.com/s'
        response = requests.get(url, headers=self.headers, params=self.params, cookies=self.cookies)
        res_data = response.content.decode()
        xpath_data = etree.HTML(res_data)
        # 匹配单个标签的内容
        # div_data = xpath_data.xpath('//div[@id="content_left"]/div[@class="result-op c-container new-pmd xpath-log"]/h3//a//text()')
        # print(div_data)
        # content = ''.join(div_data)
        # print(content)
        # print(content.strip())
        # print(content.replace('\n', '').replace(' ', ''))
        # 匹配所有标签的内容
        # contains()方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含所传入的属性值，就可以完成匹配
        div_list_data = xpath_data.xpath("//div[@id='content_left']/div[contains(@class,'c-container')]")
        for single_data in div_list_data:
            content = single_data.xpath('./h3/a//text()')
            print(" ".join(content).strip())
            print("+".join(content).strip())

    def main(self):
        self._xpath()


if __name__ == '__main__':
    spider = Spider()
    spider.main()


