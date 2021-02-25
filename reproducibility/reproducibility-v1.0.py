import random

'''
生成10个随机数，统计其中重复出现的数字及重复次数
'''

nums = [random.randrange(21) for _ in range(10)]
print(nums)

length = len(nums)
states = [0] * length

samenums = []
diffnums = []

for i in range(length):
    if states[i] != 0:
        continue
    # flag = False
    count = 0
    for j in range(1 + i, length):
        if states[j] != 0:
            continue
        if nums[i] == nums[j]:
            # flag = True
            # states[j] = 1
            count += 1
            states[j] = count

    if count:
        states[i] = 1
        samenums.append((nums[i], count + 1))
    else:
        diffnums.append(nums[i])

print(samenums)
print(diffnums)
