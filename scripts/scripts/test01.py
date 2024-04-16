"""
使用Selenium自动化浏览网页的示例。

该脚本不接受参数，也不返回任何值。
"""

from time import sleep

from selenium import webdriver
# 使用Chrome浏览器驱动
# driver=webdriver.Chrome()
driver = webdriver.Firefox()
# 访问百度网站
driver.get('http://www.baidu.com')

# 停留5秒,也可以不导入time包，直接使用time.sleep(5)

sleep(5)
# 关闭浏览器
driver.quit()
