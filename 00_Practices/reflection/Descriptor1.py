class A:
    def __init__(self) -> None:
        print("A().init-----")
        self.a = 100

    def __get__(self, instance, owner):
        print("get-" * 20)
        print(self,"aaaaaaaaa")
        print(instance,"bbbbbbbbb")
        print(owner,"cccccc")
        print("get-" * 20)
        return self

    def __set__(self, instance, value):
        print("set-" * 20)
        print(self)
        print(instance)
        print(value)
        print("set-" * 20)
        instance.__dict__['x'] = value + 200

    # def __delete__(self, instance):
    #     print(instance)
    def __repr__(self) -> str:
        return "<A {}>".format(self.a)

class B:
    x = A()
    def __init__(self):
        print("B().init=====")
        self.x = 200
        # self.__dict__['x'] = 200

if __name__ == "__main__":
    b = B()
    # print(b.x.a)
    # print(B.x,"222")
    print()
    print(B.__dict__)
    print(b.__dict__)
    print()
    print(b.x, "++++++++")
    print(b.__dict__['x'])
