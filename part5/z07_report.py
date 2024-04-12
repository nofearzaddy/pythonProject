import unittest

from part5.HTMLTestRunner import HTMLTestRunner

# 使用套件对象，加载对象 去添加用例方法
suite = unittest.defaultTestLoader.discover('.', 'z05_pa1.py')
# 实例化第三方的运行对象并运行套件对象
# HTMLTestRunner()
# stream=(sys.stdout, 测试报告的文件对象（open）,注意要使用 wb 打开
# verbosity)=(1, 可选，报告的详细程度，默认1 简略，2 详细
# title)=(None,可选，测试报告标题，默认为None
# description)=None可选，测试报告描述，python的版本 ，pycharm 版本默认为None

# file = 'report.html'
file = 'report1.html'
with open(file, 'wb') as f:  # 这里 file是变量，不需要加引号了
    # runner = HTMLTestRunner(f)  # 运行对象
    runner = HTMLTestRunner(f,2,'测试报告','python3.6.8')  # 运行对象

    # 运行对象执行套件，要写在with 缩进中
    runner.run(suite)
