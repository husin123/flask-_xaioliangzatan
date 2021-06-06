from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
from pathlib import Path
from time import sleep
from selm.gales import settings


class Gale():

    def __init__(self, implicitly_wait=12):
        option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        option.add_experimental_option(
            "excludeSwitches", ['enable-automation', 'enable-logging'])
        # 初始化driver
        self.driver = webdriver.Chrome(options=option)
        # 设置浏览器窗口大小
        # self.driver.maximize_window()
        self.driver.set_window_rect(-7, 0, 1190, 1047)
        # 设置隐性等待时间
        self.driver.implicitly_wait(implicitly_wait)

    def get_url(self, url: str):
        '''页面访问

        Args:
            url (str): url地址
        '''
        self.driver.get(url)

    def get_url_by_cookies(self, url: str, cookies_path: Path):
        '''带cookies的页面访问

        Args:
            url (str): 登录网址
            cookies_path (Path): cookies储存地址
        '''

        self.get_url(url)
        cookies = json.loads(open(cookies_path).read())
        for c in cookies:
            self.driver.add_cookie(c)
        self.get_url(url)
        # self.driver.refresh()

    def get_cookies(self, url: str, file_path: Path, user_data: dict, input_time: int = 12):
        '''获取cookies

        Args:
            url (str): 登录网址
            file_path (Path): cookies储存路径
            user_data (dict): 用户登录数据
            {
                "账号":(css_selector, str),
                "密码":(css_selector, str),
                ...
                "login": css_selector
            }
            input_time (int, optional): Defaults to 12. 用户输入验证码的时间
        '''

        self.get_url(url)
        for i in user_data:
            if i == 'login':
                continue
            for selector, content in user_data[i]:
                self.find_by_selector(selector).send_keys(content)
                # button_cache.send_keys(content)
        # 等待用户手动输入验证码
        sleep(input_time)
        self.find_by_selector(user_data["login"]).click()
        cookies = self.driver.get_cookies()
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(cookies))

    def find_by_id(self, id):
        '''通过id查找元素

        Args:
            id (str): id路径

        Returns:
            WebElement: WebElement对象
        '''

        return self.driver.find_element_by_id(id)

    def find_by_selector(self, selector):
        '''通过css属性查找webelement元素

        Args:
            selector (str): css属性

        Returns:
            WebElement: WebElement对象
        '''

        return self.driver.find_element_by_css_selector(selector)

    def find_by_xpath(self, xpath):
        '''通过xpath查找元素

        Args:
            xpath (str): xpath路径

        Returns:
            WebElement: WebElement对象
        '''

        return self.driver.find_element_by_xpath(xpath)

    def wait_clickable(self, ele_path, by="selector", time=10):
        '''等待元素可以被点击
        '''

        if by == "selector":
            return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ele_path)))
        elif by == "xpath":
            return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(
                (By.XPATH, ele_path)))
        else:
            raise TypeError(f"not type {by}")

    def wait_presence(self, ele_path, by="selector", time=10):
        '''显性等待元素出现,如果元素在规定时间内出现就返回该元素

        Args:
            ele_path (str): 与by对应的属性路径
            by (str, optional): Defaults to "selector". [还可以是xpath等]
            time (int, optional): Defaults to 10. [默认的显性等待时间]

        Raises:
            TypeError: 不存在的by方法

        Returns:
            WebElement: 如果元素在规定时间内被查找到则返回该元素WebElement对象
        '''

        if by == "selector":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ele_path)))
        elif by == "xpath":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(
                (By.XPATH, ele_path)))
        else:
            raise TypeError(f"not type {by}")

    def wait_not_presence(self, ele_path, by="selector", time=10):
        '''等待元素不存在
        '''

        if by == "selector":
            return WebDriverWait(self.driver, time).until_not(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ele_path)))
        elif by == "xpath":
            return WebDriverWait(self.driver, time).until_not(EC.presence_of_element_located(
                (By.XPATH, ele_path)))
        else:
            raise TypeError(f"not type {by}")

    def wait_visibility(self, ele_path, by="selector", time=10):
        '''等待元素对用户可见
        '''

        if by == "selector":
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ele_path)))
        elif by == "xpath":
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(
                (By.XPATH, ele_path)))
        else:
            raise TypeError(f"not type {by}")

    def wait_invisibility(self, ele_path, by="selector", time=10):
        '''等待元素对用户不可见
        '''

        if by == "selector":
            return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, ele_path)))
        elif by == "xpath":
            return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(
                (By.XPATH, ele_path)))
        else:
            raise TypeError(f"not type {by}")

    def save2png(self, file_name):
        '''获取当前浏览器窗口屏幕截图

        Args:
            file_name (str): 图片名(图片默认存放到data目录下)
        '''

        file_path = settings.DATA_DIR / file_name
        self.driver.get_screenshot_as_file(str(file_path))
        sleep(1)

    def close(self):
        '''关闭当前窗口
        '''

        self.driver.close()

    def quit(self):
        '''关闭整个浏览器
        '''

        self.driver.quit()

    def refresh(self):
        '''刷新
        '''
        self.driver.refresh()
