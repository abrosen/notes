#generates n triangle numbers
def triangleNumbers(n):
    nums =[1]
    for i in range(2,n):
        nums.append(i + nums[-1])
    return nums
    
print triangleNumbers(10)
