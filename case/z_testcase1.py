# 1，导包
import unittest


# 2，自定义测试类,需要继承unittest模块中的Te
# stCase类
class TestDemo1(unittest.TestCase):

    # 3，编写测试方法,即 用例代码，代替目前没有真正的用例代码，用print
    # 书写要求，测试方法必须以 test_开头（本质是以test开头）
    def test_method1(self):
        print("测试方法1-1")

    def test_method2(self):
        print("测试方法1-2")