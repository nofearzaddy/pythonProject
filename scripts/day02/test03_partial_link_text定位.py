'''
需求：
使用partial_link_text定位方式，使用注册A.html 页面，点击，访问新浪网站链接地址
 方法:
    1.driver.find_element_by_partial_link_text("")#定位元素方法
    2.click()点击方法
注意:
    link_text:
        1.只能定位a标签
        2.link_text定位元素的内容可以模糊部分值，但是必须代表唯一性
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
# 使用link_text定位 使用模糊，唯一代表词
# driver.find_element_by_partial_link_text("访问").click()
#没有使用唯一代表词，默认操作符合条件的第一个元素
driver.find_element_by_partial_link_text("新浪").click()
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
