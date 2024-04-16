# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Firefox()

# 打开url
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 查找用户名元素
username = driver.find_element_by_id('userA')
# 查找密码元素
passward = driver.find_element_by_id('passwordA')
# 用户名输入admin send_keys("内容")
username.send_keys('admin')
# 密码输入123456
passward.send_keys('123456')
# 暂停3秒

sleep(3)
# 退出浏览器
driver.quit()
