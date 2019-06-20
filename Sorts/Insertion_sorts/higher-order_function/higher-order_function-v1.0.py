import random
l1 = list(range(1,10))
random.shuffle(l1)
print(l1,"\n")

def sort(lst,asc = True):
    result = list()
    for x in lst:
        for i,y in enumerate(result):
            flag = x < y if asc == True else x > y
            if flag:
                result.insert(i,x)
                break
        else:
            result.append(x)
    return result

print(sort(l1,False))
print(sort(l1))
