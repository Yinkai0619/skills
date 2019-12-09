#!/usr/bin/env python3


def bisect_insert(order_list, i):
    ret = order_list[:]
    low = 0
    high = len(ret) 

    while low < high:
        mid = (low + high) // 2
        if ret[mid] < i:
            low = mid + 1
        else:
            high = mid
    ret.insert(low, i)

    return ret

if __name__ == "__main__":
    origin = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51]
    # origin = [37, 99, 73]
    origin = sorted(origin)

    l = origin
    for x in (40, 50, 100):
        l = bisect_insert(l, x)
        print(l)
