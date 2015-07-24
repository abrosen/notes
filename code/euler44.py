"""
pentagonal numbers are of the form

  n*(3n-1)/2
The difference between successive numbers is 3n - 2, where n is the largest
adding 2 successive numbers yields 3n**2 -4n  + 2  
http://www.math-magic.com/misc/pentagonal.htm
"""

import math

def penta(limit):
    n = 1
    while n <= limit:
        yield int((n*(3*n - 1))/2)
        n = n + 1


def main():
    nums = list(penta(3000))
    for i,x  in enumerate(nums[1001:]):
        for y in nums[i+1:]:
            if  x+y  in nums:
                if y-x in nums:
                    print(x, y,x+y, y-x)
                    return

if __name__ == '__main__':
    main()
