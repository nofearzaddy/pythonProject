'''
目标：unittest框架——TestCase使用
步骤：
    1，导包 import unittest
    2，新建类，并继承 unittest.TestCase
    3,测试方法必须以test开头
案例：
    编写求和测试函数
'''
import unittest


# 编写求和测试函数
def add(a, b):
    return a + b


# 创建测试类,并继承unittest.TestCase
class Test01(unittest.TestCase):
    # 创建测试方法，注意以test开头
    def test_add(self):
        # 调用要测试的函数
        result = add(1, 2)
        print(result)
        print("__name__内置变量获取当前模块名：", __name__)
    def test_add2(self):
        result = add(2, 2)
        print(result)
    if __name__ == '__main__':
        unittest.main()
