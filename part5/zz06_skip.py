import unittest

version = 29


class TestDemo(unittest.TestCase):
    @unittest.skip("跳过test_1,没有原因")
    def test_1(self):
        print("test_1")

    @unittest.skipIf(version >= 30, "版本大于等于30，不用测试")
    def test_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")
