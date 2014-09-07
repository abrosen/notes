import math
def sumOfSquares(nums):
    return sum(map(lambda x: x**2.0, nums))



def squareOfSums(nums):
    return sum(nums)**2.0

# computes squares of sums for for 1..n
def squareOfSumsNaturals(n):
    return (n*(n+1)/2.0)**2.0


# computes sum of squares for for 1..n
# square pyramidal number
def sumOfSquaresNaturals(n):
    return (n*(n+1)*(2*n +1 ))/6.0

def main():
    n =100
    print squareOfSumsNaturals(n) -  sumOfSquaresNaturals(n)


if __name__ == '__main__':
    main() 