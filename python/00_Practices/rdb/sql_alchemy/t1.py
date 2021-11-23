from ast import Str
import os
from sre_constants import IN
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


print(repr(Student.__table__))
s = Student(name='tom')
s.age = 30
print(s)

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Session
Session = sessionmaker(bind=engine)     # 构建Session类
session = Session()     # session实例