# 导包
from selenium import webdriver
import time

# 获取浏览器对象
driver = webdriver.Chrome()
# 打开url
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
# 查找电话并输入20210528
driver.find_element_by_class_name("telA").send_keys("20210528")
# 查找邮箱输入528528.@qq.com
driver.find_element_by_name("emailA").send_keys("528.@qq.com")
# 暂停3秒
time.sleep(3)
# 退出浏览器
driver.quit()
