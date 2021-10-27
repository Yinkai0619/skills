def fib1(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


def fib2(n, pre=0, cur=1):
    pre, cur = cur, pre + cur
    if n == 0:
        return pre
    return fib2(n - 1, pre, cur)


for i in range(1, 4000):
    print(fib2(i), end=', ')
