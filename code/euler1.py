# finds the sum of all numbers<limit that are multiples of x or y 
def sumOfMultiples(x,y,limit):
    total = 0
    for i in range(1,limit):
        if (not (i % x)) or (not (i%y)):
            total =  total + i
    return total

if __name__ == '__main__':
    print sumOfMultiples(3,5,1000)
    print sumOfMultiples(3,5,2000)
