import math

def isPrime(num):
    if num == 1:
        return False
    for i in xrange(2,num/2 +1):
        if num % i  == 0:
            return False
    return True

def largestPrimeFactor(num):
    """returns the largest prime factor"""
    i =  2
    largest = i
    while i < math.sqrt(num):
        if num % i == 0:
            largest = i
            num = num/i
        else:
            i= i+1
    if i < num:
        return num
    return i
    
def seiveEratosthenes(limit):
    """
    generates all prime numbers less than limit
    http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    nums = dict.fromkeys(range(2,limit), True)     
    for i in range(2,int(math.sqrt(limit))):
        if nums[i]  == False:
            continue
        for j in range(i+1,limit):
            if nums[j] == False:
                continue
            if j % i == 0:
                nums[j] =  False
    primes =  [x for x in nums.keys() if nums[x]]
    return primes


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



