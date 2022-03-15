import enum
import os
import random
import string
from ast import Str
from operator import not_
from re import I
from sre_constants import IN
from traceback import print_tb

from sqlalchemy import (Column, Date, Enum, Integer, String, and_,
                        create_engine, not_, or_, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.state import InstanceState
from sqlalchemy.sql.functions import concat
from sqlalchemy.sql.sqltypes import CHAR, INTEGER, VARCHAR, Enum, SmallInteger

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

# region Mapper
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
# endregion


# Session
Session = sessionmaker(bind=engine)     # 构建Session类
session = Session()     # session实例



class GenderEnum(enum.Enum):    #Enumerate for Python
    M = 'M'
    F = 'F'

# region User Table
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
        # return "<{}: id={} login_name={} first_name={} last_name={} gender={} age={} phone={} password={}>".format(
        #     self.__class__.name, self.id, self.login_name, self.first_name, self.last_name, self.gender, self.age, self.phone, self.password
        # )
        return "<id={} login_name={} first_name={} last_name={} gender={} age={} phone={} password={}>".format(
            self.id, self.login_name, self.first_name, self.last_name, self.gender.value, self.age, self.phone, self.password)
# endregion


class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column('emp_no', Integer, primary_key=True)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(GenderEnum), )
    birth_date = Column(Date, nullable=False)
    hire_date = Column(Date, nullable=False)

    def __repr__(self) -> str:
        return "<{}: Employee no={} name='{} {}' brith={} gender={}>".format(
            self.__class__.__tablename__, self.emp_no, self.first_name, self.last_name, self.birth_date, self.gender
        )

# print(repr(Employee.__table__))

# region drop & create
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)
# endregion



# region Insert
def get_password(length=8, chars=string.ascii_letters+string.digits):
    return ''.join([random.choice(chars) for i in range(length)])
# e = Employee(emp_no=2)
# e.first_name="Bai"
# e.last_name="Na"
# e.birth_date='1989-12-14'
# e.gender='F'
# e.hire_date='2014-08-15'
# print('1111111111111', e)

# jinxue = Employee(emp_no=3, first_name="Jin", last_name="Xue", gender="M", birth_date="1993-03-16", hire_date="2017-05-16")
# huangyao = Employee(emp_no=4, first_name="Huang", last_name="Yao", birth_date="1979-10-16", gender="F", hire_date="2014-05-16")
# try:
#     # session.add(e)
#     # session.add(jinxue)
#     session.add_all([jinxue, huangyao])
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()


# for i in range(1,10):
#     user = User(id=i, login_name="U"+str(i), first_name="User", last_name=str(i), gender=random.choice("FM"), age=random.randint(23,45), phone="13" + str(random.randint(3,9)) + str(random.randint(10000000, 99999999)), password=get_password(8))
#     print('33333333333', user)
#     try:
#         session.add(user)
#         session.commit()
#     except Exception as e:
#         print(e)
#         session.rollback()

# yinkai = User(login_name="yinkai", first_name="Li", last_name="Yinkai", gender='M', age=36, phone="13" + str(random.randint(3,9)) + str(random.randint(10000000, 99999999)), password=get_password(8))
# nana = User(login_name="nana", first_name="Bai", last_name="Na", gender='F', age=32, phone="13" + str(random.randint(3,9)) + str(random.randint(10000000, 99999999)), password=get_password(8))
# try:
#     session.add_all([yinkai, nana])
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()


# endregion




# region update
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
# endregion


# region Delete
# try:
#     session.query(User).delete()
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()


# endregion


# Select
def showresults(items):
    for i in items:
        print(i)
        print('-' * 50)

# employees = session.query(Employee)     # select * from student
# showresults(employees)
# for employee in employees:
#     print(employee)

# users = session.query(User)   # SELECT * FROM user;
# showresults(users)

# user = session.query(User).get(5)   # select * from User where id = 5;
# print(user)

# users = session.query(User).filter(User.id >= 5)    # select * from User where id >= 5;
# users = session.query(User).filter(User.id != 5)    # select * from User where id <> 5;

# users = session.query(User).filter(User.id != 5).filter(User.gender == 'F')    # select * from User where id <> 5 AND gender = 'F';
# users = session.query(User).filter(User.id != 3).filter(User.gender == GenderEnum.F)    # select * from User where id <> 3 AND gender = 'F';
# users = session.query(User).filter(and_(User.id != 3, User.gender == GenderEnum.F))     # select * from User where id <> 3 AND gender = 'F';
# users = session.query(User).filter((User.id != 3) & (User.gender == GenderEnum.F))     # select * from User where id <> 3 AND gender = 'F';

# users = session.query(User).filter(or_(User.id < 3, User.id > 7))     # select * from User where id < 3 OR id > 7;
# users = session.query(User).filter((User.id < 3) | (User.id > 7))     # select * from User where id < 3 OR id > 7;


# users = session.query(User).filter(not_(User.id > 5))    # select * from User where id <> 5;
# users = session.query(User).filter(~(User.id > 5))    # select * from User where id <> 5;
# users = session.query(User).filter(~((User.id < 3) | (User.id > 7)))     # select * from User where NOT (id < 3 OR id > 7);

# users = session.query(User).filter(User.id.in_([3,5,9]))    # SELECT * FROM User WHERE id IN (3,5,9);

# users = session.query(User).filter(User.id.notin_([3,5,9]))    # SELECT * FROM User WHERE id NOT IN (3,5,9);
# users = session.query(User).filter(~User.id.in_([3,5,9]))    # SELECT * FROM User WHERE id NOT IN (3,5,9);

# users = session.query(User).filter(User.phone.like('137%'))     # SELECT * FROM user WHERE phone LIKE '137%';
# users = session.query(User).filter(User.last_name.like('N%'))     # SELECT * FROM user WHERE last_name LIKE 'N%';
# users = session.query(User).filter(User.last_name.ilike('n%'))     # SELECT * FROM user WHERE lower(last_name) LIKE lower('N%');
# users = session.query(User).filter(User.last_name.notilike('n%'))     # SELECT * FROM user WHERE lower(last_name) NOT LIKE lower('N%');

# users = session.query(User).filter(User.phone.notlike('137%'))     # SELECT * FROM user WHERE phone NOT LIKE '137%';
# users = session.query(User).filter(~User.phone.like('137%'))     # SELECT * FROM user WHERE phone NOT LIKE '137%';

# users = session.query(User).filter(User.id >= 5).order_by(User.id)    # select * from User where id >= 5 ORDER BY id;
# users = session.query(User).filter(User.id >= 5).order_by(User.id.desc())    # select * from User where id >= 5 ORDER BY id DESC;
# users = session.query(User).filter(User.id >= 5).order_by(User.id.desc()).order_by(User.age)    # select * from User where id >= 5 ORDER BY id DESC, age;
# users = session.query(User).filter(User.id >= 5).order_by(User.id.desc(), User.age.asc())    # select * from User where id >= 5 ORDER BY id DESC, age ASC;

# users = session.query(User).order_by(User.id.asc()).limit(2)    # select * from User ORDER BY id ASC LIMIT 2;
# users = session.query(User).order_by(User.id.asc()).limit(2).offset(3)    # select * from User ORDER BY id ASC LIMIT 3,2;

# showresults(users)


# users = session.query(User).filter(User.id > 5)
# users = session.query(User).filter(User.id > 5)
# print(users)
# print("Count::::::::::::::: ", users.count())
# print(list(users))
# print(users.all())
# print(users.one())
# print(users.scalar())
# print(users.first())


# users = session.query(User).filter(User.id > 5)
result = session.query(User.gender, func.count(User.id), func.min(User.age), func.max(User.age), func.avg(User.age), func.sum(User.age)).group_by(User.gender)
# print('rrrrrrrrrrrrr',result)
# print('oooooooooooo',result.one())
# print('ssssssssssssssssss',result.scalar())         # 在one中取第一项
print(result.all())