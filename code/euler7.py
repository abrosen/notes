import math
# the nth prime number is approximately n * ln(n)

# generates all prime numbers less than limit
def seiveEratosthenes(limit):
    nums = dict.fromkeys(range(2,limit), True)     
    for i in range(2,int(math.sqrt(limit))):
        if nums[i]  == False:
            continue
        for j in range(i+1,limit):
            if nums[j] == False:
                continue
            if j % i == 0:
                nums[j] =  False
    return nums

def main():
    n =  10
    limit = int(n * math.log(n)) + 1
    print seiveEratosthenes(limit) 

if __name__ == '__main__':
    main()