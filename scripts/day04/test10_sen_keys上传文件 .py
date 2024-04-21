# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver import ActionChains
# 获取浏览器驱动对象
driver = webdriver.Firefox()
#设置元素等待。隐式等待
driver.implicitly_wait(10)


# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
# driver.find_element_by_css_selector("[name='upfilea']").click()
#正确实现
driver.find_element_by_css_selector("[name='upfilea']").send_keys(r"C:\Users\34778\Desktop\屏幕截图 2024-02-27 182227.png")
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
