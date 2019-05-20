import unittest

# import backend test modules
from test import test_PointCloudReader
from test import test_cmdarguments

#initialize the test suit
loader = unittest.TestLoader()
suite = unittest.TestSuite()

#add test to the test suite
suite.addTest(loader.loadTestsFromModule(test_PointCloudReader))
suite.addTest(loader.loadTestsFromModule(test_cmdarguments))

#initialize a runner, pass it your suit and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)