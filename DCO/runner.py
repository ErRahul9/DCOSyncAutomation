import json
import os.path
import sys
from sys import argv
# from main import main
# from  databaseConn import  connecters
# from jsonReader import jsonReader
# from config import globals
from dotenv import load_dotenv
from mainDCO import *
from auto.databaseConn import connecters
from auto.getMethods import getMethods
from auto.jsonReader import jsonReader


class runner():

    def __init__(self):
        load_dotenv()
        self.ROOTDIR = sys.path[1]
        # self.testObj = testObj
        self.adv = sys.path[0]
        self.fixpath = os.path.join(self.adv,"fixtures")
        self.jsonObject = jsonReader(self.fixpath, "{0}_Test.json".format(self.testObj)).readJson()
        # self.test = test

    def run(self, objs):
        print(self.test)
        beeswaxInfo = {}
        # objs = self.test
        getMethods(self.mod, objs).refreshSecurityToken()
        cmpType = ""
        campId = ""
        main().refreshSecurityToken()

        # sqlQuery = self.queries(campId)
        # print(response)
        # getResponseCode = response["ResponseMetadata"]
        # if getResponseCode["HTTPStatusCode"] == 200:
        #     lineItemId = connecters(sqlQuery).connectToPostgres()
        #     if len(lineItemId) == 0:
        #         print("no record found in the database")
        #     else:
        #         print(lineItemId[0][0])
        #         beeswaxData = getMethods(self.mod, objs).verifyBeeswax(lineItemId[0][0])
        # beeswaxInfo[campId] = beeswaxData
        # print(beeswaxData)

if __name__ == '__main__':
    print(runner().run())