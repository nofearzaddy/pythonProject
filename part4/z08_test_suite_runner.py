import  unittest

from part4.z08_test import TestAdd

#实例化套件对象
suite = unittest.TestSuite()
#添加测试方法
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(TestAdd))
#实例化执行对象
runner = unittest.TextTestRunner()
runner.run(suite)
