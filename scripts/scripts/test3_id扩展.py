# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Firefox()
# 打开url
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
# 查找元素用户名并输入admin
driver.find_element_by_id("userA").send_keys("admin")
# 查找元素密码框并输入123456
driver.find_element_by_id("passwordA").send_keys("123456")
# 暂停3秒
sleep(3)
# 关闭浏览器驱动对象
driver.quit()
