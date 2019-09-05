import json
import pymysql
import os
from datetime import datetime, date, timedelta


class Gundam:
    def __init__(self, gndm):
        self.id = gndm['id']
        self.name = gndm['name']
        self.pilot_name = gndm['pilot_name']
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_pilot_name(self):
        return self.pilot_name

##########################

def checkStringLengthValid(self, value):
    nameLength = value.length
    if (nameLength > 15):
        return True
    else:
        return False
    
def checkStringAlNum(self, value):
    return value.isalnum()

def checkifSentenceCase(self, value):
    return value.istitle



def default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    return super().default(obj)


def insertOne(event, context):
    con = pymysql.connect(
        host=os.environ.get('MYSQL_DB_HOST'),
        user=os.environ.get('MYSQL_DB_USER'),
        password=os.environ.get('MYSQL_DB_PASSWORD'),
        db=os.environ.get('MYSQL_DB_SCHEMA'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    cur = con.cursor()
    g = Gundam(json.loads(event["body"]))
    id = g.get_id
    name = g.get_name
    pilot = g.get_pilot_name
    cur.execute("INSERT INTO gundam VALUES (" + id + ", '" + name
                + "', '" + pilot + "');")
    con.commit()

    body = {
        "message": "insertOne",
        "input": g
        }
    response = {
        "statusCode": 200,
        "body": json.dumps(body, default=default)
    }
    return response
