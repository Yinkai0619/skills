#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/6/30 下午5:56
'''

nums_list = [
    [3, 5, 9, 1, 6, 8, 4, 7, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 3, 2, 4],
    [1, 1, 1, 1, 2]
]

nums = [0] + nums_list[0]  # 准备数据和哨兵[0]
print(nums[1:])
length = len(nums)

for i in range(2, length):  # 因为[0]为哨兵位，所以从第2个索引位开始取数
    nums[0] = nums[i]
    j = i - 1
    if nums[0] < nums[j]:  # 如果比较数大于哨兵数
        while nums[0] < nums[j]:  # 大于哨兵的数全部右移一位
            nums[j + 1] = nums[j]
            j -= 1  # 比较数指针向左移
        nums[j + 1] = nums[0]

print(nums[1:])
