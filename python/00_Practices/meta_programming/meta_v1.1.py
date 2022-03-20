import os

os.system('clear')

class Field:
    def __init__(self, name:str=None, *, pk=False, nullable=False) -> None:
        self.name = name
        self.pk = pk
        self.nullable = nullable

    def __repr__(self):
        return '<Field {}>'.format(self.name)
    
class ModelMeta(type):
    def __new__(cls, name, bases, attrs:dict):
        print(cls)
        print(name)
        print(bases)
        print(attrs)

        # 表名
        tblname = '__tablename__'
        if tblname not in attrs.keys():
            attrs[tblname] = name.lower()

        # 主键
        pks = []
        for k,v in attrs.items():
            if isinstance(v, Field):
                # print(k, '-----------------')
                # print(v.name, "~~~~~~~~~~~~~")
                if v.name is None:
                    v.name = k
                if v.pk:
                    pks.append(v)

        attrs['__primarykeys__'] = pks

        return super().__new__(cls, name, bases, attrs)

class MetaBase(metaclass=ModelMeta):
    pass

class User(MetaBase):
    __tablename__ = 'user'
    id = Field(pk=True, nullable=False)
    name = Field('username', nullable=False)
    age = Field()

class emp(MetaBase):
    id = Field(pk=True)
    name = Field()            

print('+' * 40)
print(User.__dict__)
print(emp.__dict__)