import unittest


class Test_Log(unittest.TestCase):
    def test_login(self):
        assert 1 == 1

    def setUp(self) -> None:
        print("用例开始执行")

    def tearDown(self) -> None:
        print("用例执行完毕")

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
