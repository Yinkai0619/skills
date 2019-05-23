
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


print(fib2(100))
fib1()
