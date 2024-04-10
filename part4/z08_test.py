# 导包
import unittest

from part4.tools2 import add


# 2，自定义测试类
class TestAdd(unittest.TestCase):
    # 3，书写测试方法（测试用例代码）
    def test_method1(self):
        if add(1, 2) == 3:
            print("测试用例1通过")
        else:
            print("测试用例1不通过")

    def test_method2(self):
        if add(10, 20) == 30:
            print("测试用例2通过")
        else:
            print("测试用例2不通过")

    def test_method3(self):
        if add(100, 200) == 30:
            print("测试用例3通过")
        else:
            print("测试用例3不通过")
