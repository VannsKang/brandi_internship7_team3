import pymysql

from config import db


def get_connection():
    return pymysql.connect(
        user=db['user'],
        password=db['password'],
        host=db['host'],
        db=db['database'],
        port=db['port'],
        charset='utf8mb4',
        autocommit='False'
    )
