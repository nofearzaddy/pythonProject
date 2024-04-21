# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver import ActionChains
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 设置隐式等待
driver.implicitly_wait(10)
# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\注册实例.html"
driver.get(url)
'''
需求：
    1，打开注册实例.html
    2，点击注册A网页
    3,填写注册A网页内容
'''
#点击注册A网页
driver.find_element_by_css_selector("#ZCA").click()
'''填写注册A页面信息'''
#用户名
driver.find_element_by_css_selector("#userA").send_keys("admin1")
#密码
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
#电话
driver.find_element_by_css_selector("#telA").send_keys("1111111")
#邮件
driver.find_element_by_css_selector("#emailA").send_keys("1111111@qq.com")
# 关闭驱动对象
driver.quit()
