#!/usr/bin/env python

'''
Computing primes in the specified range.
'''

primes = list()
max = int(input("Please a maximum number: "))

for i in range(1,max,2):
    for j in range(2,i):
        if not i%j:
            break
    else:
        primes.append(i)
print('List of prime Numbers: ',primes)
