import os
import pymysql
from pymysql.cursors import DictCursor

os.system("clear")

HOST = "172.27.0.1"
PORT = 3306
DB = "test"
USER = "pytest"
PWD = "pytestpass"

try:
    conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PWD, database=DB)
    print(conn.ping(False))

    cursor = conn.cursor(DictCursor)
    # insert_sql = "insert into user (login_name, age, phone, password) VALUES ('tom', 20, '18273457689', sha('pass4tom'))"
    # row = cursor.execute(insert_sql)
    # conn.commit()
    # user_id = "2"
    # sql = 'select * from user where id = {}'.format(user_id)
    
    # 参数化查询，解决SQL注入问题
    # user_id = "2"
    # sql = 'select * from user where id = %s'    
    # row = cursor.execute(sql, (user_id,))
    sql = 'select * from user where gender = %(gender)s and age > %(age)s'
    cursor.execute(sql, {'gender':'M', 'age':20})

    # print(row)
    # print(1, cursor.fetchone())
    # print(2, cursor.fetchmany(2))
    print(3, cursor.fetchall())
    # print(cursor.rownumber())
    print(cursor.rowcount())
except:
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()