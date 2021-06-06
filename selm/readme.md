# Gale说明文档

> 这是基于Python Selenium封装的库,封装了selenium常用的功能,便于中心的自动化测试

## 依赖安装

```python
# 安装依赖包
pip install -r requirements.txt
# 添加该项目到项目路径
python addProject.py
```

这是基于Chrome浏览器的自动化测试  
所以你还需要下载:  
[Chrome](http://www.google.cn/chrome/browser/desktop/index.html?standalone=1&platform=win64)  
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

注意:

- Chrome与ChromeDriver必须版本对应,否则会因为兼容性问题无法使用
- ChromeDriver下载并解压完以后会得到一个可执行文件 **chromedriver.exe**,放到 **Script/**目录下或把该文件添加到系统环境变量里

## 使用说明

**首先实例化一个Gale对象:**  

```python

    driver = Gale()
```

**页面访问:**

```python

    # 方式一: 正常的页面访问
    driver.get_url(url)

    # 方式二: 带cookies的页面访问
    driver.get_url_by_cookies(url, cookies_path)
```

**cookies的获取:**

```python

    driver.get_cookies(url, file_path, user_data, input_time = 12)

#     user_data格式参考
#     user_data = {
#     "账号": [(css_selector, user_name)],
#     "密码": [(css_selector, user_password)],
#     "login": css_selector
# }
```

**网页元素查找:**

```python
    # 通过xpath查找
    driver.find_by_xpath(xpath)
    # 通过css_selector查找
    driver.find_by_selector(selector)
```

**显性等待:**

```python

    # 显性等待元素出现,如果元素在规定时间内出现就返回该元素,
    # 默认使用css_selector选择器查找元素,等待时间为10s,下同
    driver.wait_presence(ele_path, by="selector", time=10)

    # 等待元素不存在
    driver.wait_not_presence(ele_path)

    # 等待元素可以被点击
    driver.wait_clickable(ele_path)

    # 等待元素对用户可见
    driver.wait_visibility(ele_path)

    # 等待元素对用户不可见
    driver.wait_invisibility(ele_path)
```

**窗口截屏:**

```python

    # file_name为存储文件名,文件默认存放到data目录下
    driver.save2png(file_name)
```

**关闭:**

```python

    # 关闭当前窗口
    driver.close()

    # 关闭当前浏览器
    driver.quit()
```