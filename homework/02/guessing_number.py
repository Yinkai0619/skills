
# Author: Li Yinkai
# Date: 2019.06.04

'''
猜数字: 功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
'''

import random

num = random.randint(0,100)
# print(num)
count = 0
while True:
    count += 1
    answer = int(input('Please enter an integer less than 3 bits: '))
    if answer > num:
        print('Greater.')
    elif answer < num:
        print('Less.')
    else:
        print('Success!')
        break
print('Answer number: ',count)
# 写的很棒~