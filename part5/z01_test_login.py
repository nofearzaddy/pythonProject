import unittest

from part5.tools import login


class TestLogin(unittest.TestCase):
    def test_username_password_ok(self):
        if login('admin', '123456') == '登录成功':
            print('测试通过')
        else:
            print('测试失败')

    def test_username_error(self):
        if login('root', '123456') == '登录失败':
            print('测试通过')
        else:
            print('测试失败')

    def test_password_error(self):
        if login('admin', '1234567') == '登录失败':
            print('测试通过')
        else:
            print('测试失败')

    def test_username_password_error(self):
        if login('aaa', '1234567') == '登录失败':
            print('测试通过')
        else:
            print('测试失败')
