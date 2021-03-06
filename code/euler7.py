import math

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

def main():
    # the nth prime number is approximately n * ln(n)
    # This is a HORRIBLE approximation, but good enough for this
    n =  20001
    limit = int(n * math.log(n)) + 1
    primes =  seiveEratosthenes(limit)
    #primes =  [x for x in nums.keys() if nums[x]]
    #print len(primes)
    #print primes
    print primes[10000]

if __name__ == '__main__':
    main()
