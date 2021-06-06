import time
import unittest

from selm.gales.gale import Gale


class Test(unittest.TestCase):
    def get_baidu(self):
        url = 'https://www.baidu.com/'
        driver = Gale()
        driver.get_url(url)
        # 找到输入元素的位置
        element = driver.find_by_id('kw')
        element.send_keys('python')
        # 点击 百度一下
        click = driver.find_by_id('su')
        click.click()
        time.sleep(5)

    def test_all(self):
        self.get_baidu()


if __name__ == "__main__":

    unittest.main()
