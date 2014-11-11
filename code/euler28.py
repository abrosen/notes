
N = 1001
intervals = N/2
skip = 2
total =  1
next = 1
for _ in xrange(intervals):
    for i in xrange(4):
        next += skip
        total += next
    skip +=2
print total