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


def getAll(event, context):
    con = pymysql.connect(
        host=os.environ.get('MYSQL_DB_HOST'),
        user=os.environ.get('MYSQL_DB_USER'),
        password=os.environ.get('MYSQL_DB_PASSWORD'),
        db=os.environ.get('MYSQL_DB_SCHEMA'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
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
    con = pymysql.connect(
        host=os.environ.get('MYSQL_DB_HOST'),
        user=os.environ.get('MYSQL_DB_USER'),
        password=os.environ.get('MYSQL_DB_PASSWORD'),
        db=os.environ.get('MYSQL_DB_SCHEMA'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
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
