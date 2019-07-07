# 使用generator实现：

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


for i in fib(50):
    print(i)
