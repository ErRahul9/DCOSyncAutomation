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
    print(testCases.get(argv[1]))
    if len(sys.argv) == 3:
        print("running test for {}".format(argv[2]))
        allTests = list(filter(lambda test: (test in argv[2]), allTests))
    for test in allTests:
        # expResponse = testCases.get(argv[1]).get(test).get("expectedResult")
        main(test, argv[1]).teardown()
        main(test, argv[1]).refreshSecurityToken()
        getResponse = main(test, argv[1]).ValidateResposeData(test)
        # if int(getResponse.get("ResponseMetadata").get("HTTPStatusCode")) == expResponse.get("statusCode") :
        #     tabledata = main(test, argv[1]).getTableData(test)



