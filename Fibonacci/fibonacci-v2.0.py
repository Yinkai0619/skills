
def fib1(n = 100):
    a,b = 0,1
    print(a,end=' ')
    while b < n:
        print(b,end=' ')
        a,b = b,a + b

def fib2(n=100):
    result = list()
    a,b = 0,1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def fib3(index=101):
    # 求指定索引项上的数值
    a,b = 0,1
    print()
    for i in range(2):
        print("{}: {}".format(i,i))
    for i in range(index-1):
        a,b = b,a+b
        print("{}: {}".format(i+2,b))

print(fib2(100))
fib1()
fib3()