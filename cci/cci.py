


#count the stairs
stairCombos = {}
stairCombos[0] = 1
stairCombos[1] = 1
def stairJumper1(num):
    if num < 0 :
        return 0
    if num in stairCombos:
        return stairCombos[num]
    else:
        stairCombos[num] =  stairJumper1(num-1) + stairJumper1(num-2) + stairJumper1(num-3)
        return stairCombos[num]
    




if __name__ == '__main__':
    print(stairJumper1(3))