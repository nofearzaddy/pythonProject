'''
需求：
    1，使用绝对路径定位 用户名 输入 admin
    2，暂停2秒
    3，使用相对路径定位 密码框 输入 123
方法：
    driver.find_element_by_xpath()

'''
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver = webdriver.Chrome()
# 打开注册A.html 页面
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
# 使用绝对路径定位 用户名 输入 admin
# driver.find_element_by_xpath("/html/body/form/div/fieldset/p[1]/input").send_keys("admin")
#使用层级结合属性 定位用户名
driver.find_element_by_xpath("//P[@id='p1']/input").send_keys("admin")
# 使用相对路径定位 密码框 输入 123
# driver.find_element_by_xpath("//input[@id='passwordA']").send_keys("123")
# 使用逻辑结合
driver.find_element_by_xpath("//input[@id='passwordA'and @placeholder='密码A']").send_keys("123")
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
