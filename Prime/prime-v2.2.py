# 求一定范伟内的质数（素数）

num = 100000
count = 1
# print(2)
for x in range(3, num, 2):
    if x > 10 and not x % 5:    # 所有大于10的质数中，个位数只有1,3,7,9。意思为能被5整除的数字为合数，不再计算
        continue
    for i in range(3, int(x**0.5) + 1, 2):  # 取模数量减半，并过滤掉偶数
        if not x % i:   # 不是素数退出循环
            # print(num, "is a composite number.")
            break
    else:
        print('Prime number: ',x)
        count += 1
print('Total number of primes: ',count)