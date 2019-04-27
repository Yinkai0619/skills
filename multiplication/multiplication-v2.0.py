#!/usr/bin/env python

for i in range(1,10):
    for j in range(i,10):
        print(str(i)+'*'+str(j)+'='+str(j*i),end = "\t")
    print()
    print('\t' * i,end='')

print()
