'''
学习TestSuite和TestRunner的使用
'''
# 1,导包（unittest）
import unittest

from part4.z07_testcase1 import TestDemo1
from part4.z07_testcase2 import TestDemo2

# 2，实例化（创建对象）套件对象
suite = unittest.TestSuite()
# 3，使用套件对象添加用例方法
# 方式一，套件对象.addTest(测试类名（’方法名‘）)#建议测试类名和方法名直接复制
# suite.addTest(TestDemo1('test_method1'))
# suite.addTest(TestDemo1('test_method2'))
# suite.addTest(TestDemo2('test_method1'))
# suite.addTest(TestDemo2('test_method2'))

# 方法二实例化TestLoader对象
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(TestDemo1))
suite.addTest(loder.loadTestsFromTestCase(TestDemo2))

# 4，实例化运行对象
runner = unittest.TextTestRunner()
# 5，使用运行对象去执行套件对象
# 运行对象。run(套件对象)
runner.run(suite)
