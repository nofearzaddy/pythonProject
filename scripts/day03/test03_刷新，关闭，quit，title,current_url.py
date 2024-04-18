# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url =r"C:\Users\34778\Desktop\02_其他资料\注册实例.html"
driver.get(url)
# 用户名输入admin 目的:刷新完成——清空
driver.find_element_by_css_selector("#user").send_keys("admin")
# 暂停3秒
sleep(3)
# 刷新
driver.refresh()
# 获取title
title = driver.title
print("当前页面title为:", title)
# 获取当前url
current_url = driver.current_url
print("当前页面url为:", current_url)
# 点击 注册A网页 打开新窗口
driver.find_element_by_partial_link_text("注册A").click()
# 关闭主窗口
driver.close()
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
