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
'''需求：
        1，点击alert按钮
        2，输入用户名admin
        '''
# 定位alert按钮并点击
driver.find_element_by_css_selector("#alerta").click()
sleep(2)
# 切换到alert对话框默认返回的是alert对话框对象
at = driver.switch_to.alert
sleep(2)
#处理alert对话框
#同意#
# at.accept()
#获取文本
print("警告信息",at.text)
#取消
at.dismiss()
# 定位用户名输入admin
driver.find_element_by_css_selector("[type='textA']").send_keys("admin")
sleep(2)

# 关闭驱动对象
driver.quit()
