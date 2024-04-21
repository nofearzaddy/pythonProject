# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
目标:默认北京A
    暂停2秒
    定位上海A
    暂停2秒
    定位广州A'''
# 使用select
'''
1,导包 Select 类
2，获取select对象
    匿名：Select(element).select_by_index()#通过下标
    实名：select=Select(element)
        调用：select.select_by_index()
    注意：
        1，Select 类是通过select标签来控制其下的ooption元素
        2,element:只能是select标签'''

el = driver.find_element_by_css_selector("#selectA")
sleep(2)
'''通过下标形式访问'''
# 切换上海
Select(el)
Select(el).select_by_index(1)
sleep(2)
Select(el).select_by_index(2)
'''通过value值形式访问'''
sel=Select(el)
sel.select_by_value("sh")
sleep(2)
sel.select_by_value("gz")
'''通过文本形式访问'''
Select(el).select_by_visible_text("A广州")
sleep(2)
Select(el).select_by_value("bj")

# 关闭驱动对象
driver.quit()
