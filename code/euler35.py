from  eulertools import seiveEratosthenes, isPrime

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""


LIMIT = 1000000

def isCircularPrime(num):
    n = str(num)
    if len(n) >1:
        if '2' in n or '4' in n or '5' in n or '6' in n or '8' in n or '0' in n:
            return False    
    rotations = getDigitRotation(num)
    for r in rotations:
        if not isPrime(r):
            return False
    return True

def getDigitRotation(num):
    num = str(num)
    rotations = []
    for i in xrange(len(num)):
        num = num[1:] + num[0]
        rotations.append(num)
    return map(int, rotations)


def doTheThing():
    primes = seiveEratosthenes(LIMIT)
    print len(primes), "primes generated"
    circularPrimes = []
    for p in primes:        
        if isCircularPrime(p):
            print p
            circularPrimes.append(p)
    print len(circularPrimes)
    

if __name__ == '__main__':
    doTheThing()
