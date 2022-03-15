from ast import Str
import os
from sre_constants import IN
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.state import InstanceState
from sqlalchemy.sql.functions import concat
from sqlalchemy.sql.sqltypes import CHAR, INTEGER, VARCHAR, Enum, SmallInteger
import enum

os.system('clear')

# print(sqlalchemy.__version__)

# Create Connect
HOST = "172.27.0.1"
PORT = 3306
DB = "test"
USER = "pytest"
PWD = "pytestpass"

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(USER, PWD, HOST, PORT, DB), echo=True)

# Declare a Mapping
Base = declarative_base()   # 基类

# Mapper
# class Student(Base):
#     __tablename__ = 'student'   # 必须定义表名
#     id = Column(Integer, primary_key=True, autoincrement=True)  # 字段定义，类属性
#     name = Column(String(48), nullable=False)
#     age = Column(Integer)

#     def __repr__(self) -> str:
#         return "<{}: {} {} {}>".format(self.__class__.name, self.id, self.name, self.age)


# print(repr(Student.__table__))

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Session
Session = sessionmaker(bind=engine)     # 构建Session类
session = Session()     # session实例



class GenderEnum(enum.Enum):    #Enumerate for Python
    M = 'M'
    F = 'F'


class User(Base):
    __tablename__ = 'user'

    id = Column('id', SmallInteger, primary_key=True, autoincrement=True)
    login_name = Column(VARCHAR(16), unique=True, nullable=False)
    first_name = Column(String(20), nullable=True)
    last_name = Column(VARCHAR(20))
    gender = Column(Enum(GenderEnum), nullable=False, default='M')
    age = Column(INTEGER)
    phone = Column(CHAR(11))
    password = Column(VARCHAR(512))

    def __repr__(self) -> str:
        # return super().__repr__()
        return "<{}: id={} login_name={} first_name={} last_name={} gender={} age={} phone={} password={}>".format(
            self.__class__.name, self.id, self.login_name, self.first_name, self.last_name, self.gender, self.age, self.phone, self.password
        )

class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column('emp_no', Integer, primary_key=True)
    brith_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(GenderEnum), )
    hire_date = Column(Date, nullable=False)

    def __repr__(self) -> str:
        return "<{}: Employee no={} name='{} {}' gender={}>".format(
            self.__class__.name, self.emp_no, self.first_name, self.last_name, self.age
        )

# print(repr(Employee.__table__))

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


# Insert
e = Employee(emp_no=1)
e.brith_date='1985-06-19'
# print(e)

session.add(e)
session.commit()

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



# Select
employees = session.query(Employee)     # select * from student
for employee in employees:
    print(employee)



