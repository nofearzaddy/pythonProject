# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\drop.html"
driver.get(url)
sleep(3)
# 实例化并获取ActionChains类
action = ActionChains(driver)
source=driver.find_element_by_css_selector("#div1")
target=driver.find_element_by_css_selector("#div2")
action.drag_and_drop(source,target).perform()
#扩展,通过坐标偏移量执行
action.drag_and_drop_by_offset(source,xoffset=360,yoffset=180).perform()
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
