import math
FILE = "p098_words.txt"

def buildDict(words):
	d = {}
	for word in words:
		k = "".join(sorted(word))
		if k not in d.keys():
			d[k] = []
		d[k].append(word)
	return d

def isSquare(number):
	return number == int(sqrt(number))**2

# newton's method
# x0 is initial guess
# f is function, g is derivative
def newtons(x0,f,g):
	x =  x0 -  (f(x0)/g(x0))
	last = x +1
	while abs(last - x) > 0.0000000001:
		last = x 
	return x
		
def sqrt(x0):
	f = lambda x: x**2 - x0
	g = lambda x: 2*x
	return newtons(x0, f, g)

	
	
def doTheThing():
	words = open(FILE).read().split(',')
	words = list(map(lambda x: x.strip('"'), words))
	d = buildDict(words)
	anagrams = []
	for combo in d:
		if len(d[combo]) > 1:
			anagrams.append(d[combo])
	print(anagrams)

if __name__ == '__main__':
	doTheThing()
