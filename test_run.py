import unittest
from unittestreport import TestRunner
from TestCase.test_login import Test_Log

suite = unittest.TestSuite()
# 创建加载器
loader = unittest.TestLoader()
# 通过类去加载
# suite.addTest(loader.loadTestsFromTestCase(Test_Log))
# 通过路径去加载
suite.addTest(loader.discover(r"/Users/git_300/python_unittest/TestCase"))
runner = TestRunner(suite)
runner.run()
