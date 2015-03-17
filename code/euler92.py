# coding=utf-8
"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""



LIMIT = 10000000


def squareDigits(num):
    retval = 0
    while num > 0:
        i =  num % 10
        retval += i*i
        num /= 10
    return retval

def doTheThing():
    nums= [0]*LIMIT
    nums[1] = 1
    for start in xrange(2,LIMIT):
        i = start
        while i != 1 and i != 89:
            i = squareDigits(i)
            if nums[i]:
                i = nums[i]
                break
        nums[start] = i


    total = 0
    for n in nums:
        if n == 89:
            total +=1
    print total


if __name__ == '__main__':
    doTheThing()