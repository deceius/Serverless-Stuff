import json
from datetime import datetime, date, timedelta
import os
import pymysql


###

class Gundam:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.pilot_name = ""

    def instantiateJSON(self, gndm):
        self.id = gndm['id']
        self.name = gndm['name']
        self.pilot_name = gndm['pilot_name']

    def instantiate(self, id, name, pilot):
        self.id = id
        self.name = name
        self.pilot_name = pilot

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_pilot_name(self):
        return self.pilot_name


def getConnection():
    con = pymysql.connect(
        host=os.environ.get('MYSQL_DB_HOST'),
        user=os.environ.get('MYSQL_DB_USER'),
        password=os.environ.get('MYSQL_DB_PASSWORD'),
        db=os.environ.get('MYSQL_DB_SCHEMA'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return con


def default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    return super().default(obj)


#### END OF HELPER / GUNDAM ###

def getAll(event, context):
    con = getConnection()
    cur = con.cursor()
    cur.execute('SELECT * from trainingDB.gundam')
    res = cur.fetchall()

    body = {
        "message": "getAll",
        "input": res
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body, default=default)
    }
    return response


def getOne(event, context):
    con = getConnection()
    cur = con.cursor()
    param = event['queryStringParameters']
    query = "SELECT * from trainingDB.gundam WHERE id = " + param["id"]
    cur.execute(query)

    res = cur.fetchone()

    body = {
        "message": "getAll",
        "input": res
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body, default=default)
    }
    return response
