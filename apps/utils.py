from datetime import timedelta, datetime
from django.db import connection
import base64, os, sys, json, pytz

IST = pytz.timezone('Asia/kolkata')
today = datetime.now().strftime("%Y%m%d")
nowtime = datetime.now().strftime("%H%M%S")


def getToday():
    now = datetime.now()
    date = now.strftime("%Y%m%d")
    return date


def getlocaltime():
    datetime_ist = datetime.now(IST)
    curr_clock = datetime_ist.strftime("%H%M%S")
    return curr_clock


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]

    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def getMaxUcode(tablename):

    getMaxUcodeQuery = f'SELECT COALESCE(MAX(ucode), 0)AS ucode FROM {tablename}'
    with connection.cursor() as c:
        c.execute(getMaxUcodeQuery)
        getMaxucode = dictfetchall(c)
        ucode = getMaxucode[0]['ucode']
        maxucode = ucode + 1
    
    return maxucode
