import random
l1 = list(range(1,10))
random.shuffle(l1)
print(l1,"\n")

def sort(lst,asc = True):
    def compare(a,b):
        return x < y if asc else x > y
    result = list()
    for x in lst:
        for i,y in enumerate(result):
            if compare(x,y):
                result.insert(i,x)
                break
        else:
            result.append(x)
    return result

print(sort(l1,False))
print(sort(l1))
