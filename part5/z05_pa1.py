# 1,导包unittest/pa
import json
import unittest

from parameterized import parameterized

from tools import login


# 组织测试数据,s数据和参数要保持一致
def build_data():
    with open('data.json', encoding='utf-8') as f:
        result = json.load(f)  # [{...},{...}]
        data = []
        for i in result:
            data.append((i.get("username"), i.get("password"), i.get("expect")))
    return data


# 2，定义测试类
class TestLogin(unittest.TestCase):
    # 3，书写测试方法
    @parameterized.expand(build_data())
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))
    # 4，组织测试数据并传参（装饰器 @ parameterized.expand(data)）
