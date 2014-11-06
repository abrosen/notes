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