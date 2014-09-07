def lcm_brute(nums):
    solution = max(nums)
    found = False
    while not found:
        solution += max(nums)
        if all(map(lambda x: solution % x == 0, nums)):
            return solution



def main(): 
    for i in xrange(3,21):
        print lcm_brute(range(2,i))


if __name__ == '__main__':
    main()