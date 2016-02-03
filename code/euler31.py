denominations = [1,2,5,10,20,50,100,200]



def makeChange(amount):
	ways = [0] * (amount+1)
	ways[0] = 1
	for d in denominations:
		for i in range(d, len(ways)):
			ways[i] += ways[i - d]
	return ways[-1]

print(makeChange(200))


