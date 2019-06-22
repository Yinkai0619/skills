# Author: Li Yinkai
# Date: 2019.06.04

'''
功能描述：
    遍历并打印0到100，如果数字能被3整除，显示Fizz；
    如果数字能被5整除，显示Buzz；
    如果能同时被3和5整除，就显示FizzBuzz。
    结果应该类似：0,1,2，Fizz，4，Buzz，6……14，FizzBuzz，16……
'''

fizz = []
buzz = list()
fizzbuzz = list()

# Algorithm1:
# num = 3
# while num <= 100:
#     if not num % 3:
#         fizz.append(num)
#         if not num % 5:
#             fizzbuzz.append(num)
#     if not num % 5:
#         buzz.append(num)
#     num += 1


# Algorithm2:
# for num in range(3,101):
#     if not num % 3:
#         fizz.append(num)
#         if not num % 5:
#             fizzbuzz.append(num)
#     if not num % 5:
#         buzz.append(num)

# Algorithm3:
fizz = list(filter(lambda x: not x % 3, list(range(101))))
buzz = list(filter(lambda y: not y % 5, list(range(101))))
fizzbuzz = list(filter(lambda z: not z % 5, fizz))

print("Fizz: ", ','.join(map(str, fizz)))
print("Buzz: ", ','.join(map(str, buzz)))
print("FizzBuzz: ", ','.join(map(str, fizzbuzz)))
# 虽然和结果有点不相符，但用到高阶函数，不错~