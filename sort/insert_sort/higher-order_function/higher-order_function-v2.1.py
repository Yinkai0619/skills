import random
l1 = list(range(1,10))
random.shuffle(l1)
print(l1,"\n")


def sort( lst,fn = lambda a,b : a > b ):
    result = list()
    for x in lst:
        for i,y in enumerate(result):
            if fn( x, y ):
                result.insert(i,x)
                break
        else:
            result.append(x)
    return result

print(sort(l1, lambda a,b : a < b ))
print(sort(l1))
