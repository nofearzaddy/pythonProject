'''
目标:
    断言练习
案例
    tpshop登录
       输入：正确用户名和密码  验证码为空
        断言：提示信息是否为，验证码不能为空！
        要求：如果断言出错，截屏保存。
'''
#导包
import unittest
from selenium import webdriver
#定义测试类并继承unittest.TestCase
class TestTphopLogin(unittest.TestCase):

#定义初始方法
    def setUp(self):
        pass
        #获取浏览器驱动对象
        self.driver = webdriver.Chrome()
        #打开url
        self.driver.get("http://localhost")

        #最大化浏览器
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(10)
    #定义teardown
    def tearDown(self):
        #关闭浏览器
        pass
    #定义登录测试方法，验证码为空
    def test_login_code_null(self):
        #点击登录链接
        driver=self.driver
        driver.find_element_by_link_text("登录").click()

        # 输入用户名
        driver.find_element_by_id("username").send_keys("admin")
        # 输入密码
        driver.find_element_by_id("password").send_keys("123456")
        # 输入验证码
        driver.find_element_by_id("verify_code").send_keys("")
        # 点击登录
        driver.find_element_by_class_selector(".J-login-submit").click()
        # 获取登录后提示信息
        text = driver.find_element_by_class_selector(".layui-layer-content").text
        #定义预期结果
        expect = "验证码不能为空！"
        # 断言
        self.assertEqual(expect, text)
        #截图
        driver.get_screenshot_as_file("../image/login_code_null.png")
        print("截图成功")
