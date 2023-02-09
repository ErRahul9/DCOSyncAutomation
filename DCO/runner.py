from sys import argv
from unittest import TestCase

from auto.jsonReader import jsonReader
from mainDCO import *
import argparse

# import testCase as testCase


if __name__ == '__main__':
    fixpath = os.path.join(sys.path[0], "fixtures")
    testFileName = argv[1] + "_test.json"
    testCases = jsonReader.jsonReader(fixpath, testFileName).readJson()
    allTests = testCases.get(argv[1]).keys()
    print(type(allTests))
    if len(sys.argv) == 3:
        print("running test for {}".format(argv[2]))
        allTests = list(filter(lambda test: (test in argv[2]), allTests))
    for test in allTests:
        # main(test, argv[1]).teardown()
        main(test, argv[1]).refreshSecurityToken()
        print(main(test, argv[1]).run(test))
