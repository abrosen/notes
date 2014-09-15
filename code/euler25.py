# generate fibnocci up to digit number of digits 
def digitFib(digits):
    fibs = [1,1]
    while len(str(fibs[-1])) <digits:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs, len(fibs)


if __name__ == '__main__':
    print digitFib(10)