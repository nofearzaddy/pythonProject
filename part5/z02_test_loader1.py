import unittest

# 2使用默认的加载对象并加载用例
suite = unittest.defaultTestLoader.discover("../case", 'z_testcase*.py')
# # 3,实例化运行对象
# runner = unittest.TextTestRunner()
# # 4,运行
# runner.run(suite)
unittest.TextTestRunner().run(suite)
