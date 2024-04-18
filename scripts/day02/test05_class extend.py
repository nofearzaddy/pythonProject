'''
需求
1,使用class  id选择器 定位用户名输入admin
2,使用css 属性选择器 定位密码框，输入123
3，使用css class 选择器定位电话号码：528528528
#4,使用css元素选择器定位span标签获取文本值
#5,使用层级选择器定位email输入528@qq.com
方法：
driver.find_element_by_css_selector()
     获取文本的方法 元素。text
'''
# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Chrome()
# 打开注册A.html 页面
url = r"D:\Study\1. 8天web自动化全套\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 1,使用class  id选择器 定位用户名输入admin 以指定字母开头 语法:[属性^='开头字母']
driver.find_element_by_css_selector("[name^='us']").send_keys("admin")
# 2,使用css 属性选择器 定位密码框，输入123  以指定字母结尾 语法:[属性$='结尾字母']
driver.find_element_by_css_selector("[name$='dA']").send_keys("123")
# 3，使用css class 选择器定位电话号码：528528528 包含指定字母 语法:[属性*='指定字母']
driver.find_element_by_css_selector("[class*='el']").send_keys("528528528")
#4,使用css元素选择器定位span标签获取文本值
span=driver.find_element_by_css_selector("span").text
print("获取span的标签文本值:",span)
#5,使用层级选择器定位email输入528@qq.com
driver.find_element_by_css_selector("p>input[placeholder='电子邮箱A']").send_keys("528@qq.com")
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
