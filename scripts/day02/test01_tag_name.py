'''
    需求:
    1.使用tag_name定位方式，使用注册A.html 页面，用户名输入admin
    方法:
    1.driver.find_element_by_tag_name("")#定位元素方法
    2.send_keys()#输入方法
    3.driver.quit()#退出方法

'''
# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Chrome()
# 打开注册A.html 页面
url=r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
# 使用tag_name定位用户名并输入admin
driver.find_element_by_tag_name("input").send_keys()
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
