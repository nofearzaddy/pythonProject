'''
    目标:




'''
# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开注册A.html 页面
url=r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
# 获取所有input标签
# elements = driver.find_elements_by_tag_name("input")
elements = driver.find_elements_by_id("userA")
print(len(elements))
print('elements的类型为：',type(elements))
# 输入内容
elements[0].send_keys("admin")
# 通过遍历来输入
for i in elements:
    i.send_keys("admin")
# 暂停3秒

sleep(3)
# 退出浏览器驱动
driver.quit()
