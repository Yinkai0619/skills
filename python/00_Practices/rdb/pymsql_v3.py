import os
import pymysql
from pymysql.cursors import DictCursor

os.system("clear")

HOST = "172.27.0.1"
PORT = 3306
DB = "test"
USER = "pytest"
PWD = "pytestpass"

conn = pymysql.connect(host=HOST, port=PORT, user=USER,
                       password=PWD, database=DB)
with conn:
    with conn.cursor() as cursor1:
        print(type(cursor1))
        for i in range(13, 16):
            insert_sql = "insert into user (login_name, gender, age) values ('user{0}', 'F', 20+{0})".format(
                i)
            cursor1.execute(insert_sql)
        conn.commit()

    with conn.cursor() as cursor2:
        sql = "select * from user"
        cursor2.execute(sql)
        print(cursor2.fetchall())
