import unittest

# 2,实例化加载对象并添加用例
# unittest.TestLoader().discover('用例所在的路径',pattern='用例文件名')
# 用例所在路径建议使用相对路径，用例的代码文件名可以使用*（任意多个任意字符）通配符
suite = unittest.TestLoader().discover('../case', '*.py')
# # 3,实例化运行对象
# runner = unittest.TextTestRunner()
# # 4,运行
# runner.run(suite)
unittest.TextTestRunner().run(suite)
