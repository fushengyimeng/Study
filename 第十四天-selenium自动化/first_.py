import time
from selenium import webdriver


class Selenium:
    def __init__(self):
        pass

    def start(self):
        # 实例化一个driver对象
        driver = webdriver.Chrome()
        # 打开百度
        driver.get('http://www.baidu.com')
        time.sleep(2)
        input_tag = driver.find_element_by_id('kw').send_keys('python')
        time.sleep(1)
        click_button = driver.find_element_by_id('su').click()
        time.sleep(5)
        print('即将关闭....')
        res = driver.page_source
        print(res)
        # 关闭浏览器
        driver.close()

    def main(self):
        self.start()

if __name__ == '__main__':
    s = Selenium()
    s.main()