denominations = [1,2,5,10,20,50,100,200]
def combinations(target):
    waysToBreak = [0]*(target+1)
    waysToBreak[0]  = 1
    for coin in denominations:
        for x in range(coin, len(waysToBreak)):
            waysToBreak[x] = waysToBreak[x] + waysToBreak[x-coin]
        print "breaking using", denominations[:denominations.index(coin)+1], waysToBreak 



print combinations(200)