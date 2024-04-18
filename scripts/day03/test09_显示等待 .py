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
'''
目标:显式等待
操作：
    1.导包 WebDriverWait()类
    2，实例化WebDriverWait()类并调用until(method)方法
    method:匿名函数
    lambda x:x.find_element_by_css_selector()
需求:
    1.定位用户名输入admin
'''
#实例化WebDriverWait()类并调用until(method)方法
#调用until()方法返回的一定是个元素
el=WebDriverWait(driver,timeout=10,poll_frequency=0.5).until(lambda x:x.find_element_by_css_selector("#user"))
#此时el还不是元素只有代码运行起来才是元素
el.send_keys("admin")
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
