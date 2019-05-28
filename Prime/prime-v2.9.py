import datetime

loop = 1
upper_limit = 100000
dalta = [0,0]
counts = [0,0]

start = datetime.datetime.now()

for _ in range(loop):
    # count = 1
    primes = []
    for x in range(2, upper_limit):
        for i in range(2, x-1):
            if not x % i:   # 不是素数退出循环
                # print(num, "is a composite number.")
                break
        else:
            # print(num, 'is a prime number.')
            # print(x)
            primes.append(x)
            # count += 1

    print('Total number of primes: ',len(primes))
    # print(primes)
    print('='*100)

dalta[0] = (datetime.datetime.now() - start).total_seconds()

start = datetime.datetime.now()

for _ in range(loop):
    # count = 1
    primes = [2]
    # print(2)
    for x in range(3, upper_limit, 2):
        if x > 10 and not x % 5:    # 所有大于10的质数中，个位数只有1,3,7,9。意思为能被5整除的数字为合数，不再计算
            continue
        for i in range(3, int(x**0.5) + 1, 2):  # 使用试除法测试，用被测试数值除以被测试数值平方根以内的数（并排除偶数）
            if not x % i:   # 不是素数退出循环
                # print(num, "is a composite number.")
                break
        else:
            # print('Prime number: ',x)
            # count += 1
            primes.append(x)

    print('Total number of primes: ',len(primes))
    # print(primes)
    print('='*100)

dalta[1] = (datetime.datetime.now() - start).total_seconds()
print(dalta)


