def generateFibonacci(limit):
    fibs = [1,2]
    nextFib = fibs[-1] + fibs[-2]
    while(nextFib < limit):
        fibs.append(nextFib)
        nextFib= fibs[-1] + fibs[-2]
    return fibs



if __name__ == "__main__":
    fibs = generateFibonacci(4000000)
    print map(lambda x: x if x % 2 == 0 else 0, f)