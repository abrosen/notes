#!/usr/bin/python

total = 0
LIMIT = 1000000
for i in range(LIMIT):
    if str(i)[::-1] == str(i):
        if bin(i)[2:] == bin(i)[-1:1:-1]:
            print(i, bin(i))
            total += i

print(total)
