# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Chrome()
# 打开url
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
# 输入admin
driver.find_element_by_id("userA").send_keys("admin")
# 输入密码 123456
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
# 输入电话 111122222
driver.find_element_by_css_selector(".telA").send_keys("111122222")
# 输入邮箱 528528528@qq.com\
driver.find_element_by_css_selector("#emailA").send_keys("528528528@qq.com")
# 暂停3秒
sleep(3)
# 修改电话号码 528528528——>清空操作
driver.find_element_by_css_selector(".telA").clear()
driver.find_element_by_css_selector(".telA").send_keys("528528528")
# 暂停3秒
sleep(3)
# 点击注册按钮
# driver.find_element_by_css_selector("[type='submitA']").click()
driver.find_element_by_css_selector("button").click()
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
