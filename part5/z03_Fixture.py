import unittest


class TestLogin(unittest.TestCase):

    def test_1(self):
        print("输入账号密码，点击登录 1")

    def test_2(self):
        print("输入错误账号密码，点击登录 2")

    def setUp(self):
        # 每个测试用例之前执行
        print('输入网址')

    def tearDown(self):
        # 每个测试用例之后执行
        print('关闭当前页面')

    @classmethod
    def setUpClass(cls) -> None:
        print('1,打开浏览器')

    @classmethod
    def tearDownClass(cls) -> None:
        print('5,关闭浏览器')
