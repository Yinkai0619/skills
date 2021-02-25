#!/usr/bin/env python

m_list = [
    [1, 9, 8, 5, 6, 7, 4, 3, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
]

c_list = m_list[1]
print("Initial:\t", c_list, "\n========================================")
length = len(c_list)
count_swap = 0
count = 0
flag = False    # 交换标记。如果某i次比较后没有发生交换，侧说明已经符合最终结果，无需再进行后续排序，退出排序过程。
for i in range(length - 1):
    # print("{},{}".format(c_list[i],c_list[i+1]))
    if flag:
        break
    for j in range(length - 1 - i):
        count += 1
        if c_list[j] > c_list[j + 1]:
            c_list[j], c_list[j + 1] = c_list[j + 1], c_list[j]
            count_swap += 1
        else:
            flag = True
        # print("{}: {}".format(j+1,c_list))
    # print()
print("Result:\t\t", c_list)
print("Count: {}\tSwap: {}".format(count, count_swap))
