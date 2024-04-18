# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver import ActionChains
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url = r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
# 输入用户名admin1
username = driver.find_element_by_css_selector("#userA")
username.send_keys("admin1")
# 删除1
username.send_keys(Keys.BACK_SPACE)

# 全选用户名 Ctrl+A
username.send_keys(Keys.CONTROL, "a")
sleep(3)

# 复制用户名 Ctrl+C
username.send_keys(Keys.CONTROL, "c")
sleep(3)

# 粘贴 将复制的用户名粘贴到密码框
driver.find_element_by_css_selector("#passwordA").send_keys(Keys.CONTROL, "v")
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
