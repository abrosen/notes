from eulertools import *
# n**2 +a*n+ b
# abs(b) must be a prime
# thus all of b's must be prime

primes = seiveEratosthenes(100000)
bList = seiveEratosthenes(1000)


largestGen=(0,0,0)

for a in xrange(-1000,1001):
    for b in bList:
        seqLen = 0
        n =  0
        while n**2 + a*n + b in primes:
            seqLen += 1
            n +=1
        if seqLen > largestGen[0]:
            largestGen=(seqLen,a,b)
            print largestGen
print "\n" 
print largestGen, largestGen[1]*largestGen[2]
