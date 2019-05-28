n = 10

def fib(n=100):
    result = list()
    i = 0
    while True:
        if i <= 1:
            result.append(i)
            i += 1
        else:
            num = result[-1] + result[-2]
            if num > n:
                break
            else:
                result.append(num)
                i += 1
    return result
print(fib(1000))
