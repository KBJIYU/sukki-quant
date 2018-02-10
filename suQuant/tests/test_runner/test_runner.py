# TODO 未來 CI 跑測試...
# 可能也可以在上層 test_main 跑..
# 再思考看看
# python -m unittest suQuant\tests\test_runner\test_runner.py

from suQuant.runner.runner import Runner

import unittest
import datetime

class TestRunner(unittest.TestCase):

    aRunner = Runner()

    def test_loadData(self):
        test_loadData

if __name__ == '__main__':
    unittest.main()
