"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
"""

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


def isPandigital(a,b,c):
    check = set(str(a)+str(b)+str(c))
    if '0' in check:
        return False
    if len(check) == 9:
        print(c,'X',b,'=',a,check)
        return True
    return False
        

def doTheThing():
    products = []
    for i in range(1000,9999):
        if len(set(str(i))) < len(str(i)):
            continue
        for j in range(2,1000):
            if i % j == 0:
                if isPandigital(i,j,i//j):
                    products.append(i)
    print(sum(set(products)))
        
        
if __name__ == '__main__':
    doTheThing()
