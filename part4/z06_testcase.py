'''
代码目的，学习TestCase(测试用例)模块的书写方法
'''
# 1，导包
import unittest


# 2，自定义测试类,需要继承unittest模块中的Te
# stCase类
class TestDemo(unittest.TestCase):

    # 3，编写测试方法,即 用例代码，代替目前没有真正的用例代码，用print
    # 书写要求，测试方法必须以 test_开头（本质是以test开头）
    def test_method(self):
        print("测试方法1")

    def test_method2(self):
        print("测试方法2")

# 4,执行用例（方法）
# 4.1将光标放在类名后面运行,会执行类中所有的测试方法
# 4.2将光标放在方法名后面运行，只执行当前方法
