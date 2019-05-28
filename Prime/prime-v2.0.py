# 求一定范伟内的质数（素数）

num = 100000
count = 1
for x in range(2, num):
    for i in range(2, x-1):
        if not x % i:   # 不是素数退出循环
            # print(num, "is a composite number.")
            break
    else:
        # print(num, 'is a prime number.')
        # print(x)
        count += 1

print(count)