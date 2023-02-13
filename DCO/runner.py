from sys import argv
from auto.jsonReader import jsonReader
from mainDCO import *



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
        main(test, argv[1]).teardown()
        main(test, argv[1]).refreshSecurityToken()
        getResponse = main(test, argv[1]).ValidateResposeData(test)




