import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SCHEMA = "mysql+pymysql"
USER = "pytest"
PWD = "pytestpass"
HOST = "172.17.0.2"
PORT = 3306
DB = "test"
engine = create_engine('{}://{}:{}@{}:{}/{}'.format(SCHEMA, USER, PWD, HOST, PORT, DB), echo=True)

Base = declarative_base()  # 基类


# Mapper
class Student(Base):
    __tablename__ = "student"  # 必须指定表名
    id = Column(Integer, primary_key=True, autoincrement=True)  # 字段定义
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<{}: {} {} {}>".format(self.__tablename__, self.id, self.name, self.age)


# print(repr(Student.__table__))

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Session
Session = sessionmaker(bind=engine)  # 构建Session会话类
session = Session()  # session实例


# Insert & Update
# s1 = Student(name="Tom")
# # print(s1)
# s1.age = 40
# # print(s1)
# s2 = Student(name="Jerry")
# s2.age = 39

# try:
#     # s1.age = 50
#     # session.add(s1)
#     session.add_all([s1, s2])
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()

# try:
#     student.age = 36
#     student.name = "Yinkai"
#     session.add(student)        # INSERT, UPDATE
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()


# Delete
# try:
#     student = session.query(Student).delete()       # DELETE FROM student
#     session.commit()
#     print(student)
# except Exception as e:
#     print(e)
#     session.rollback()

# try:
#     s = session.query(Student).get(4)
#     session.delete(s)       # DELETE FROM student WHERE student.id = 4;
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()


# Query
# student = session.query(Student)      # SELECT * FROM student;
# for s in student:
#     print(s)
# print(list(student))

# student = session.query(Student).get(4)     # SELECT * FROM student WHERE id = 2;
# print(student)

# s3 = Student(id=4, name="Jerry", age=39)
# try:
#     session.delete(s3)
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()
# s1 = Student(1, "Yinkai", 36)
# s2 = Student(2, "Nana", 30)


# State
def getstate(i, entity):
    from sqlalchemy.orm.state import InstanceState
    state: InstanceState = sqlalchemy.inspect(entity)
    state = "session_id={}, attached={} || transient={}, pending={}, persistent={}, deleted={}, detached={}".format(
        state.session_id, state._attached, state.transient, state.pending, state.persistent, state.deleted,
        state.detached
    )
    print(i, ": ", state)
    print('-' * 50, end="\n")


s = Student()
getstate(1, s)

s = Student(id=6)
s.name = "Tom"
s.age = 31
try:
    session.add(s)
    getstate(2, s)
    session.commit()
    getstate(3, s)
except Exception as e:
    print(e)
    getstate(4, s)
    session.rollback()

s = session.query(Student).get(6)
# for i in s:
#     print(i)
getstate(5, s)

s.name = "Tony"
s.age = 34
try:
    session.add(s)
    getstate(6, s)
    session.commit()
    getstate(7, s)
except Exception as e:
    print(e)
    getstate(8, s)
    session.rollback()

try:
    session.delete(s)
    getstate(9, s)
    session.flush()
    getstate(10, s)
    session.commit()
    getstate(11, s)
except Exception as e:
    print(e)
    getstate(12, s)
    session.rollback()

################################################################################################
# s1 = Student(id=1)
# s1.name = "Yinkai"
# s1.age = 36
# s2 = Student(id=2)
# s2.name = "Nana"
# s2.age = 30
# try:
#     session.add_all([s1, s2])
#     # session.add(s1)
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()

# students = session.query(Student)
# for student in students:
#     if student.name == "Yinkai":
#         try:
#             session.delete(student)
#             session.commit()
#         except Exception as e:
#             print(e)
#             session.rollback()
#     print(student)
