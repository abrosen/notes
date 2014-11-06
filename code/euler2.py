def generateFibonacci(limit):
    """Returns the list of all fibonacci numbers < limit

    Please make limit > 3
    The returned list is A000045 compliant
    http://oeis.org/A000045
    """
    fibs = [0,1,1,2]
    nextFib = fibs[-1] + fibs[-2]
    while(nextFib < limit):
        fibs.append(nextFib)
        nextFib= fibs[-1] + fibs[-2]
    return fibs



if __name__ == "__main__":
    fibs = generateFibonacci(4000000)
    print fibs
    # zero out all non-even numbers
    fibs  =  map(lambda x: x if x % 2 == 0 else 0, fibs) 
    print fibs
    print sum(fibs)
