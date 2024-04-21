# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver import ActionChains
# 获取浏览器驱动对象
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 设置隐式等待
driver.implicitly_wait(10)
# 打开url
url = "http://www.baidu.com"
driver.get(url)
# 设置cookie
driver.add_cookie({'name': 'BDUSS',
                   'value': '2Z5ZW4xd2NweWY5NjU0RUZ0YnZqNW5QeDl6VlV0UVZyVnUxelJRMVNCMlBpa3htSVFBQUFBJCQAAAAAAAAAAAEAAADOvcLx1MLSubqu07AxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI~9JGaP~SRmQ'})
sleep(5)
driver.refresh()
sleep(5)
# 获取所有cookie信息
# cookies = driver.get_cookies()
# print("cookies内容为",cookies)
# for co in cookies:
#     print(co['name'])
cookie = driver.get_cookie("BDUSS")
print("cookie",cookie)

'''
目标:
    cookie操作
案例： 使用cookie绕过百度登录
步骤：
    1，手动登录百度网站
    2，手动获取登录后的cookies 'BDUSS' 
    3，使用selenium 内的add_cookie(name='BDUSS',value='xxxx')'''
# 使用select

# 关闭驱动对象
driver.quit()
