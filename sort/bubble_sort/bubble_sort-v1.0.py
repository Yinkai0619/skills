#!/usr/bin/env python

m_list = [
    [1,9,8,5,6,7,4,3,2],
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,4,3,2,1]
]

c_list = m_list[1]
print("Initial:\t",c_list)
print("=================================")
length = len(c_list)
count_swap = 0
count = 0
for i in range(length):
    #print("{},{}".format(c_list[i],c_list[i+1]))
    for j in range(length-1-i):
        count += 1
        if c_list[j] > c_list[j+1]:
            c_list[j],c_list[j+1] = c_list[j+1],c_list[j]
            count_swap += 1
        #print("{}: {}".format(j+1,c_list))
    #print()
print("Result:\t\t",c_list)
print("Count: {}\tSwap: {}".format(count,count_swap))
