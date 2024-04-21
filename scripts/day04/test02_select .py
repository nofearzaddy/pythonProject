# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver import ActionChains
# 获取浏览器驱动对象
driver = webdriver.Firefox()
#最大化浏览器
driver.maximize_window()
#设置隐式等待
driver.implicitly_wait(300)
# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
'''
目标:默认北京A
    暂停2秒
    定位上海A
    暂停2秒
    定位广州A'''
#使用css定位来操作
sleep(2)
driver.find_element_by_css_selector("[value='sh']").click()
# 暂停3秒
sleep(3)
driver.find_element_by_css_selector("[value='gz']").click()

# 关闭驱动对象
driver.quit()
