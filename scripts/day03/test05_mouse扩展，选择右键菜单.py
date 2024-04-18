# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
# 实例化并获取ActionChains类
action = ActionChains(driver)
# 定位用户名 在用户名上右击鼠标 预期:粘贴
# 获取用户名元素

user = driver.find_element_by_css_selector("#userA")
action.context_click(user).perform()
user.send_keys("p")
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
