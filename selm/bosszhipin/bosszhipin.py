# -*- encoding: utf-8 -*-
'''
@File    :   bosszhipin.py
@Time    :   2021/06/22 20:29:28
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
# 爬取boss直聘信息并存入data目录 待续...

import csv
import time

from selm.gales.gale import Gale


class Zhuaqu:
    def __init__(self):
        self.url = 'https://www.zhipin.com/beijing/'
        self.driver = Gale()

    def get_data(self):
        self.driver.get_url(self.url)
        # 登录
        denglu = self.driver.find_by_xpath(
            '//*[@id="header"]/div[1]/div[4]/div/a[5]')
        denglu.click()
        # 扫码登录
        saoma = self.driver.find_by_xpath(
            '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[2]')
        saoma.click()
        # 等待扫码
        time.sleep(10)
        for i in range(10, 100):
            # python 搜索的url
            target_url = 'https://www.zhipin.com/c101010100/?query=python&page=3&ka=page-' + \
                str(i)
            self.driver.get_url(target_url)
            # 此页内容
            ul_text = self.driver.find_by_xpath(
                '//*[@id="main"]/div/div[2]/ul')
            # 解析 text
            self.parse_data(ul_text)

        # 下一页面访问
        # next_page = self.driver.find_by_xpath(
        #     '//*[@id="main"]/div/div[3]/div[3]/a[5]')
        # next_page.click()
        self.driver.quit()

    def parse_data(self, ul_text):
        # 解析text
        li_texts = ul_text.find_elements_by_tag_name("li")
        for li_text in li_texts:
            data = ''
            text = li_text.text
            data += text
            self.save_data(data)

    def save_data(self, data):
        # 储存数据
        res = data.split('\n')
        # res = ['职位名称', '位置', '薪资', '工作年限', '联系人', '公司名称', '所需技能', '福利']
        data_filepath = r'D:/Code\xaioliangzatan/selm/bosszhipin/data/result.csv'
        with open(data_filepath, 'a+', encoding="utf-8", newline='') as f:
            outputwriter = csv.writer(f)
            outputwriter.writerow(res)
            f.close()


if __name__ == '__main__':
    obj = Zhuaqu()
    obj.get_data()
