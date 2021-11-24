from ast import Str
import os
from sre_constants import IN
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.state import InstanceState

os.system('clear')

# print(sqlalchemy.__version__)

HOST = "172.27.0.1"
PORT = 3306
DB = "test"
USER = "pytest"
PWD = "pytestpass"

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(USER, PWD, HOST, PORT, DB), echo=True)

Base = declarative_base()   # 基类

# Mapper
class Student(Base):
    __tablename__ = 'student'   # 必须定义表名
    id = Column(Integer, primary_key=True, autoincrement=True)  # 字段定义，类属性
    name = Column(String(48), nullable=False)
    age = Column(Integer)

    def __repr__(self) -> str:
        return "<{}: {} {} {}>".format(self.__class__.name, self.id, self.name, self.age)


# print(repr(Student.__table__))

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Session
Session = sessionmaker(bind=engine)     # 构建Session类
session = Session()     # session实例


# Insert
# s = Student(name='Yinkai')
# s.age = 30
# # print(s)

# session.add(s)
# session.commit()

# try:
#     s.age = 36      # update student set age = 36 where name = 'Yinkai'
#     session.add_all([s])
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()

#
# yinkai = Student(name="Yinkai", age=36)
# # yinkai.id=1
# # yinkai.name='Yinkai'
# # yinkai.age=36
# nana = Student(name="Nana", age=30)
# try:
#     session.add_all([yinkai, nana])
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()

    



# Update    先查才能后改
# student = session.query(Student).get(2)     # select * from student where id = 2; get的查询对象是主键
# print(student)

# student.name = 'Nana'
# student.age = 30
# try:
#     session.add(student)
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()

# yinkai = session.query(Student).get(5)
# nana = session.query(Student).get(6)
# try:
#     yinkai.id=1
#     nana.id=2
#     session.add_all([yinkai, nana])
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()




# Delete 
# s = session.query(Student).get(1)       # 先查后才能删除
# try:
#     session.delete(s)
#     session.commit()      # delete 
# except Exception as e:
#     print(e,"~~~~~~~~~")
#     session.rollback()

# try:
#     session.query(Student).delete()
#     session.commit()    # DELETE FROM student
# except Exception as e:
#     print(e)
#     session.rollback()



# Select
# students = session.query(Student)     # select * from student
# for student in students:
#     print(student)



# 查看状态
def getstate(i, entity):
    state:InstanceState = sqlalchemy.inspect(entity)
    state = "session_id={}, attached={}, transient={}, pending={}， persistent={}, deleted={}, detached={}".format(
        i, state.session_id, state._attached, state.transient, state.pending, state.persistent, state.deleted, state.detached
    )
    print("id={}:".format(i),  state)
    print('-' * 30, end='\n\n')

# s1 = session.query(Student).get(1)
# s2 = Student()
# getstate(1, s1)
# getstate(2, s2)
# try:
#     s3 = Student(name="tom", age=40)
#     session.add(s3)
#     getstate(3, s3)
#     session.commit()
#     getstate(4, s3)
# except Exception as e:
#     print(e)
#     session.rollback()
#     getstate(5, s3)

# tom = session.query(Student).get(7)
# try:
#     getstate(6, tom)
#     tom.id=3
#     session.add(tom)
#     getstate(7, tom)
#     session.commit()
#     getstate(8, tom)
# except Exception as e:
#     print(e)
#     session.rollback()
#     getstate(8, tom)

try:
    s = session.query(Student).get(8)
    getstate(9, s)
    session.delete(s)
    getstate(10, s)
    session.flush()
    getstate(11, s)
    # session.commit()
    getstate(12, s)
except Exception as e:
    print(e)
    session.rollback()





# ss = session.query(Student)
# for s in ss:
#     print(s)



