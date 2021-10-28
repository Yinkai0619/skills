import pymysql

USER = "pytest"
PWD = "pytestpass"
HOST = "172.27.0.1"
PORT = 3306
DB = "test"

try:
    conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PWD, database=DB)
    print(conn.ping(False))
finally:
    if conn:
        conn.close()