def reverse(i):
    return int(str(i)[::-1])


def isPalimdrone(i):
    return str(i) == str(i)[::-1]


def computeLychrels(limit):
    lychrels = limit
    for x in range(limit):
        isLychrel = True
        attempts = 1
        while attempts < 60:
            x = x + reverse(x)
            if isPalimdrone(x):
                isLychrel = False
                break
            attempts += 1
        if not isLychrel:
            lychrels -= 1
    return lychrels


def main():
    print(computeLychrels(10000))

if __name__ == '__main__':
    main()
