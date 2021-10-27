import pymysql


conn = None
cursor = None

try:
    conn = pymysql.connect(host="localhost", user="pytest", password="pytestpass", database="test", port=33061)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # insert_sql = "INSERT INTO user (login_name, first_name, last_name, password) VALUES ('user1', 'user', '1', sha('user1pass'))"
    # cursor.execute(insert_sql)

    user = "'user"
    id = "12 or 1=1"
    # pwd = "user12pass"
    # pwd = "12345' or 'a'='a"
    # sql = "SELECT * FROM user WHERE login_name='{}' and password = '{}'".format(user, pwd)
    # sql = "SELECT * FROM user WHERE login_name={}".format(user)
    sql = "SELECT * FROM user WHERE id=%s"#.format(user)
    print(sql)
    count = cursor.execute(sql, (id))
    # print(count)

    # rows = cursor.fetchone()
    # rows = cursor.fetchmany(2)
    rows = cursor.fetchall()
    print(rows)
    print(cursor.rowcount, cursor.rownumber)

    
    # conn.commit()
except Exception as e:
    # conn.rollback()
    print(e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()