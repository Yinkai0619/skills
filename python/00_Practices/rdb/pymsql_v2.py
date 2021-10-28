import os
import pymysql
from pymysql.cursors import DictCursor

os.system("clear")

HOST = "172.27.0.1"
PORT = 3306
DB = "test"
USER = "pytest"
PWD = "pytestpass"

conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PWD, database=DB)
# print(conn.ping(False))
try:
    with conn.cursor() as cursor:
        for i in range(6, 7):
            insert_sql = "insert into user (login_name, age) values ('user{0}', 20+{0})".format(i)
            rows = cursor.execute(insert_sql)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    if conn:
        conn.close()


