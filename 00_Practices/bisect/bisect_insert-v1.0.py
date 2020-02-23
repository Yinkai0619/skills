#!/usr/bin/env python

'''
有一个无序序列[37, 99, 73, 48, 47, 40, 40, 25, 99, 51]，对其先排序出新列表。
分别尝试插入一些数字到这个新序列中合适的位置，保证其有序。
'''


origin = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51]
# origin = [37, 99, 73, 48]   # 37, 48, 73, 99
newlist = sorted(origin)
print(newlist)

def insert_sort(orderlist, i):
    ret = orderlist[:]
    low = 0
    high = len(ret) # -1

    while low < high:
        mid = (low + high) // 2 # 2
        if orderlist[mid] < i:
            low = mid + 1
        else:
            high = mid
    ret.insert(low, i)
    return ret

l = newlist
for x in (20,80,70,100):
    l = insert_sort(l, x)
    print(l)

