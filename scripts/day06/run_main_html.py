
# 导包
import unittest

from scripts.tool.HTMLTestRunner import HTMLTestRunner

# 定义 测试套件
suite = unittest.defaultTestLoader.discover("./", pattern="test02*.py")
# 执行
with open("../report/report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)
