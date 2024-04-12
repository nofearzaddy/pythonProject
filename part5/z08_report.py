import unittest

# 导入自定义的HTML测试报告类
from part5.HTMLTestRunnerCN import HTMLTestReportCN

# 组装测试用例集合，这里使用默认的测试加载器从当前目录加载所有以'pa1.py'结尾的测试用例
suite = unittest.defaultTestLoader.discover('.', '*pa1.py')

# 实例化一个HTML报告生成器对象，并准备写入到文件'report_cn.html'中
with open('report_cn.html', 'wb') as f:
    # 初始化HTMLTestReportCN对象，将测试结果输出为HTML格式，保存到文件中
    runner = HTMLTestReportCN(f)
    # 运行测试套件，并生成HTML测试报告
    runner.run(suite)
