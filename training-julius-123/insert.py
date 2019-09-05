import json
import pymysql
import os
from datetime import datetime, date, timedelta


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
    value = json.loads(event["body"])
    name = value["name"]
    pilot = value["pilot_name"]
    cur.execute("INSERT INTO gundam VALUES (0, '" + name
                + "', '" + pilot + "');")
    con.commit()

    body = {
        "message": "insertOne",
        "input": value}
    response = {
        "statusCode": 200,
        "body": json.dumps(body, default=default)
    }
    return response
