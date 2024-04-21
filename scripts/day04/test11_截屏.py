# 导包
import time

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
url = r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
'''
目标：截屏
方法：1，driver.get_screenshot_as_file(file_path)
需求1，输入用户名
    2，截屏 当前目录下 admin.png
    
'''
#输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin")
#调用截屏方法
# driver.get_screenshot_as_file("./admin.png")
#存放指定目录
driver.get_screenshot_as_file("../image/admin.png")
#动态获取文件名称使用时间戳
driver.get_screenshot_as_file("../image/%s.png" % (int(time.strftime("%y_%m_%d_%H_%M_%S"))))
time.sleep(3)
# 关闭驱动对象
driver.quit()
