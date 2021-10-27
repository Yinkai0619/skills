#!/usr/bin/env python

for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print(str(j)+'*'+str(i)+'='+str(j*i),end = "\t")
        else:
            print(end='\n')
            break

print(end='\n')
