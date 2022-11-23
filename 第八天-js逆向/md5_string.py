from hashlib import md5
import time

def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()



if __name__ == '__main__':

    url = "https://hz.meituan.com/meishi/api/poi/getPoiList?cityName=杭州&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=2833209422&uuid=07c883a792db432fa77e.1618385045.1.0.0&platform=1&partner=126&originUrl=https://hz.meituan.com/meishi/&riskLevel=1&optimusCode=10"
    l = str(time.time()*1000).split('.')[0]
    str =l + url
    print(str)
    print(encrypt_md5(str))
