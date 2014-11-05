import math
#generates n triangle numbers
def triangleNumbers(n):
    #for i in range(2,n):
    #    nums.append(i + nums[-1])
    return map(lambda x: x*(x+1)/2, range(1, n))

def trinagleNumberGen(n):
    i = 0
    while i <= n:
        yield i*(i+1)/2
        i += 1

def primeFactorization(num):
    factors = []
    i = 2
    while(num > 1 and i <= num):
        if num % i == 0:
            factors.append(i)
            num = num/i
        else:
            i= i+1
    return factors

def divisors(n):
    d = [1]
    for i in xrange(2,n/2 +1):
        if n%i ==0:
            d.append(i)
    d.append(n)
    return d

def numDivisors(n):
    num = 1
    primes = primeFactorization(n)
    for x in set(primes):
        num = num * (1 + primes.count(x))
    return num


for i in trinagleNumberGen(50000000):
    d = numDivisors(i)
    print i, d
    if d > 500:
        break