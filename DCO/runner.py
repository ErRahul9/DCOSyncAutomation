from unittest import TestCase
from mainDCO import *
import argparse
# import testCase as testCase



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='running DCO tests for thresholds')
    parser.add_argument('testName',default="all")
    # parser.argument_default('All')
    tests = parser.parse_args()
    print(parser.parse_args())


    #
    #
    #
    # def runTests(self):
    #     main().run(TestCase)
    #     self.assertTrue(True)
