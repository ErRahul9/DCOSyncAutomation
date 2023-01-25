from datetime import datetime
import json
import os
import subprocess
import sys
import uuid

import boto3
from auto.databaseConn import connecters

from auto import *


class main():
    def __init__(self,test):
        self.test = test
        self.mod = sys.argv[1]
        self.ROOTDIR = sys.path[1]
        # self.testObj = testObj
        self.campPath = sys.path[0]
        self.fixPath = os.path.join(self.campPath, "fixtures")
        print(len(sys.argv))
        if len(sys.argv) == 2:
            file = open(os.path.join(self.fixPath, '{0}_test.json'.format(self.mod)))
            jsonCampaignSync = json.load(file)
            self.testObj = jsonCampaignSync.get(self.mod)
            # print([keys for keys in testObj.keys()])
            self.test = [keys for keys in self.testObj.keys()]
        else:
            self.test = [sys.argv[2]]

    def refreshSecurityToken(self):
        p = subprocess.Popen(['okta-awscli', '--profile', 'core', '--okta-profile', 'core'])
        print(p.communicate())


    def updatePayload(self,tests):
        dt = datetime.now()
        pay = self.testObj.get(tests).get("payload")
        pay["transactionId"] = str(uuid.uuid4())
        pay["batchId"] = str(uuid.uuid4())
        pay["timestamp"] = str(dt.isoformat())+"Z"
        return pay

    def run(self,tests):
        # for tests in self.test:
        message = self.updatePayload(tests)
        sqs_client = boto3.client("sqs", region_name="us-west-2")
        url = self.testObj.get(tests).get("queueUrl")
        groupId = uuid.uuid4()
        response = sqs_client.send_message(
            QueueUrl=url,
            MessageBody=json.dumps(message),
            MessageGroupId= "QA_Automation_Test",
            # MessageGroupId="QA_Automation_Test",
            MessageDeduplicationId=str(uuid.uuid4()) + ":Automationtest"
        )
        print(message)
        return  response



    def getTableData(self):
        for tests in self.test:
            responses = self.run(tests)
            if responses.get("ResponseMetadata").get("HTTPStatusCode") == 200:
                data  = self.testObj.get(tests).get("databaseInformation")
                key = data.get("key")
                val = self.updatePayload(tests).get("campaignId")
                data = data.get("getColmn")
                sql = "select {} from sync.campaign_thresholds where {} = {}".format(data,key,val)
                print(sql)
                result = connecters(sql).connectToPostgres()
                expectedVal = result[0][0]
                compField = self.testObj.get(tests).get("payload").get("threshold")
                if expectedVal == compField:
                    print("expected value {} is matching the data in database {}".format(expectedVal,compField))
                else:
                    print("expected value {} is not matching the data in database {}".format(expectedVal, compField))












if __name__ == '__main__':
    main("test").refreshSecurityToken()
    # print(main("DSOPublisherPerformanceThreshold").run())
    print(main("DSOPublisherPerformanceThreshold").getTableData())
    # campaign budgets, daily budget (bx) , open market cap messages , blocklist,
