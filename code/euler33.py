"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

"""
We're talking about digits here, two of each in the numerator and denominator, but 2 are the same.

So we can have for answers (cancelling the x terms)
ax / xb = a/b  (we know we have at lest one of these)
ax / bx = a/b , sans 0
xa / xb = a/b
xa / bx = a/b

"""
from functools import reduce

def doTheThing():
    ans = []
    for a in range(1,10):
        for x in range(1,10):
            for b in range(1,10):
                num = a*10 + x
                dem = x*10 + b
                if num == dem:
                    break
                frac = float(a)/b
                if float(num)/dem  == frac:
                    ans.append( (num,dem) )
    num = reduce(lambda x, y: x*y,   map(lambda x: x[0],  ans))
    dem = reduce(lambda x, y: x*y,   map(lambda x: x[1],  ans))
    print(num,dem)

if __name__ == '__main__':
    doTheThing()