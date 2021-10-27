import pymysql
import os

# os.system("clear")

conn = pymysql.connect(host="localhost", user="pytest", password="pytestpass", database="test", port=33061)
# print(conn)
with conn:
    # cursor = conn.cursor()
    with conn.cursor() as cursor:
        # print(type(cursor), "-" * 20, cursor)
        # id = "12 or 1=1"
        uid = "12"
        sql = "SELECT * FROM user WHERE id>%s"
        # sql = "SELECT * FROM user WHERE id=12"
        print(sql)
        # count = cursor.execute(sql)
        count = cursor.execute(sql, uid)

        rows = cursor.fetchall()
        print(rows)
        print(cursor.rowcount, cursor.rownumber)
        # cursor.close()

# conn.close()
