# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url =r"C:\Users\34778\Desktop\02_其他资料\注册A.html"
driver.get(url)
#实例化并获取ActionChains类
action=ActionChains (driver)
#定位用户名 在用户名上右击鼠标 预期:粘贴
#获取用户名元素
user=driver.find_element_by_css_selector("#userA")
# #调用右击方法
action.context_click(user).perform()
sleep(3)

#发送用户名并双击 预期:选中admin
pwd=driver.find_element_by_css_selector("#passwordA")
pwd.send_keys("123456")
# sleep(3)
action.double_click(pwd).perform()
# # sleep(3)
#移动到注册按钮上 预期: 按钮变色，出现 加入会员
action.move_to_element(driver.find_element_by_css_selector("button")).perform()
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
