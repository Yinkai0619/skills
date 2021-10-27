import pymysql


conn = None
cursor = None

try:
    conn = pymysql.connect(host="localhost", user="pytest", password="pytestpass", database="test", port=33061)
    cursor = conn.cursor()

    # for i in range(12,15):
    #     insert_sql = "INSERT INTO user (id, login_name, first_name, last_name, password) VALUES ({}, 'user{}', 'user', '{}', 'user{}pass')".format(i,i,i,i)
    #     count = cursor.execute(insert_sql)
    insert_sql = "INSERT INTO user (id, login_name, first_name, last_name, password) VALUES (%s, %s, %s, %s, %s)"#.format(i,i,i,i)
    count = cursor.executemany(insert_sql, [('{}'.format(i), 'user{}'.format(i), 'user', '{}'.format(i), 'user{}pass'.format(i)) for i in range(20, 26)])

    conn.commit()
    print(count)
except Exception as e:
    conn.rollback()
    print(e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

