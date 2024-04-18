# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

#将浏览器最大化
driver.maximize_window()
#暂停3秒
sleep(3)
#设置固定大小 300 200
driver.set_window_size(300,200)
#暂停2秒
sleep(2)
#移动浏览器窗口位置 x:320，y:150
driver.set_window_position(320,150)
#暂停2秒
sleep(2)
#最大化\
driver.maximize_window()

#点击访问新浪网站  注意:要演示后退功能，必须先执行打开新的网站
driver.find_element_by_partial_link_text("访问").click()
#暂停2秒
sleep(3)
#执行后退——>注册A.html
driver.back()
#暂停2秒
sleep(2)
#执行前进——>新浪 ：注意 前进必须放到后退操作后执行
driver.forward()

# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
