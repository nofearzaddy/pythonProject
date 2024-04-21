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
driver.implicitly_wait(30)
# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
'''
需求：
    1.启动暂停2秒
    2滚动条拉到最后'''
sleep(2)
#1，设置js控制滚动条语句
js="window.scrollTo(0,10000)"
# 2，调用执行js语句方法
driver.execute_script(js)
sleep(2)

# 关闭驱动对象
driver.quit()
