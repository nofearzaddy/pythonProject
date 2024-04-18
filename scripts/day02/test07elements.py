'''
    目标:
        driver.find_element()
    需求:
        1.使用 driver.find_element()方法
        2，输入用户名：admin
        3,输入密码:123456



'''
# 导包
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开注册A.html 页面
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 使用driver.find_element()定位用户名
driver.find_element(By.ID, "userA").send_keys("admin")
# 使用driver.find_element()定位密码
driver.find_element(By.CSS_SELECTOR, "#passwordA").send_keys("123456")
# 暂停3秒

sleep(3)
# 退出浏览器驱动
driver.quit()
