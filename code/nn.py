import random
def forwardMultiplyGate(x,y):
	return x*y

def forwardAddGate(x,y):
	return x + y

def forwardCircuit(x,y,z):
	return forwardMultiplyGate(forwardAddGate(x,y),z)


def solveRandom(f,x,y):
	""" Given a function and two inputs, we search for the output with the greatest value.
	We do this by randomly tweaking the inputs
	"""
	bestOut = float("-inf")
	bestX = x
	bestY = y
	step = 0.01
	trials = 0 
	while trials < 10000:
		xCand = x + step * (random.random() * 2 -1)
		yCand = y + step * (random.random() * 2 -1)
		out = f(xCand,yCand)
		if out > bestOut :
			bestOut =  out
			bestX = xCand
			bestY = yCand
		trials += 1
	return bestX, bestY, bestOut

def solveNewtons

x = -2
y =  5
z = -4
print solveRandom(forwardMultiplyGate, -2,3)
print forwardCircuit(x,y,z)
