# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url =r"C:\Users\34778\Desktop\02_其他资料\注册实例.html"
driver.get(url)
#获取用户名文本框大小
size=driver.find_element_by_css_selector("#user").size
print("用户名大小为:",size)
#获取页面上第一个超文本链接内容
text=driver.find_element_by_css_selector("a").text
print("页面中第一个a标签为:",text)
# 获取页面上第一个超文本链接地址（href属性）
att=driver.find_element_by_css_selector("a").get_attribute("href")
print("页面中第一个a标签的href属性为:",att)
#判断span元素是否可见
display=driver.find_element_by_css_selector("span").is_displayed()
print("span元素是否可见:",display)
#判断 取消按钮是否可用
enable=driver.find_element_by_css_selector("#cancel").is_enabled()
print("取消按钮是否可用:",enable)
#判断旅游是否被选中
selected=driver.find_element_by_css_selector("#ly").is_selected()
print("旅游是否被选中:",selected)
# 暂停3秒
sleep(3)
# 关闭驱动对象
driver.quit()
