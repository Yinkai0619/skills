# 判断一个数是否为质数（素数）

num = 19477

for i in range(2, num):
    if not num % i:
        print(num, "is a composite number.")
        break
else:
    print(num, 'is a prime number.')
