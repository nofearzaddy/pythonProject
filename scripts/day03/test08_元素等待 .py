# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver import ActionChains
# 获取浏览器驱动对象
driver = webdriver.Firefox()
#设置元素等待。隐式等待
driver.implicitly_wait(10)

# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
'''
目标:隐式等待
'''
#给以个错误的id，不能找到，如果直接抛出异常，说明等待失效，如果在设置的指定时长以外抛出异常，说明等待有效
driver.find_element_by_css_selector("#user").send_keys("admin")
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
