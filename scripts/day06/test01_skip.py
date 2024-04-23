"""
    目标：unittest skip 与 skipif功能
    语法：
        @unittest.skip("原因")
        @unittest.skipIf(条件，原因)
"""
import  unittest
version=30
class Test01(unittest.TestCase):
    # 1，定义测试方法
    @unittest.skip("暂未完成")
    def test01(self):
        print("test01")
        '''功能暂未完成'''
        pass
    @unittest.skipIf(version>25,"版本大于25，跳过此用例")
    def test02(self):
        print("test02")
        pass