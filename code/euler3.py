import math
def largestPrimeFactor(num):
    """returns the largest prime factor"""
    i =  2
    largest = i
    while i < math.sqrt(num):
        if num % i == 0:
            largest = i
            num = num/i
        else:
            i= i+1
    if i < num:
        return num
    return i

def main():
    print largestPrimeFactor(600851475143)

if __name__ == '__main__':
    main()