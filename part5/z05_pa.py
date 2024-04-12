# 1,导包unittest/pa
import unittest
from parameterized import parameterized

from part5.tools import login

# 组织测试数据,s数据和参数要保持一致
data = [
    ('登录成功', 'admin', '123456'),
    ('登录失败', 'root', '1234567'),
    ('登录失败', 'admin', '1234567'),
    ('登录失败', 'root', '123456'),
]


# 2，定义测试类
class TestLogin(unittest.TestCase):
    # 3，书写测试方法
    @parameterized.expand(data)
    def test_username_password_ok(self, expect, username, password):
        self.assertEqual(expect, login(username, password))
    # 4，组织测试数据并传参（装饰器 @ parameterized.expand(data)）
