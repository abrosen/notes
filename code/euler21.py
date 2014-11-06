def properDivisors(n):
    """returns a list of all the divisors of n, excluding n"""
    d = [1]
    for i in xrange(2,n/2 +1):
        if n%i ==0:
            d.append(i)
    return d

def aliquotSum(n):
    """returns the aliquot sum, the sum of n's perfect divisors"""
    return sum(properDivisors(n))



if __name__ == '__main__':
    sums = {}
    amicableNums = []
    for i in xrange(2,10000):
        sums[i] = aliquotSum(i)
        if sums[i] <i and sums[i] in sums.keys(): 
            if i == sums[sums[i]]:
                amicableNums.append(i)
                amicableNums.append(sums[i])
    print amicableNums, sum(amicableNums)