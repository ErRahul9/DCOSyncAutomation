import psycopg2
import os
from dotenv import load_dotenv



class connecters():
    def __init__(self,query):
        load_dotenv()
        self.host = os.environ['POSTGRES_HOST']
        self.user = os.environ['POSTGRES_USER']
        self.pwd = os.environ['POSTGRES_PW']
        self.port = os.environ['POSTGRES_PORT']
        self.db = os.environ['POSTGRES_DATABASE']
        self.query = query

    def connectToPostgres(self):
        conn = psycopg2.connect(database=self.db, user=self.user, password=self.pwd, host= self.host, port=self.port)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(self.query)
        results =  cursor.fetchall()
        conn.commit()
        conn.close()
        return results
#
if __name__=="__main__":
    q = "select * from sync.campaign_thresholds where campaign_id = 164100"
    print(connecters(q).connectToPostgres())