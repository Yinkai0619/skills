class B:
    B = 200

class A(B):
    Z = 100
    d = {}
    def __init__(self,x,y) -> None:
        self.x = x
        setattr(self, 'y', y)
        # self.__dict__['a'] = 5

    def __getattribute__(self, item):
        print(item, '----')
        # return object.__getattribute__(self, item)
        # return 1
        raise AttributeError

    def __getattr__(self, item):
        print('__getattr__: ', item)
        # return self.d[item]
        return 'aaa'

    # def __setattr__(self, name: str, value: str) -> None:
    #     print(name, value)
    #     # setattr(self, name, value)
    #     # self.__dict__[name] = value
    #     self.d[name] = value
    
    # def __delattr__(self, name: str) -> None:
    #     print("Delete {} with __delattr__".format(name))

if __name__ == "__main__":
    a = A(1,2)
    print(A.__dict__)
    print(a.__dict__)
    print(a.x)
    print(a.d)
    # print(a.k,"===")
    # print(a.a,"-----")
    # del a.a
    # del a.__dict__['a']
    # print(a.a,"-----")