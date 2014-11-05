import random
def forwardMultiplyGate(x,y):
	return x*y

def forwardAddGate(x,y):
	return x + y

def forwardCircuit(x,y,z):
	return forwardMultiplyGate(forwardAddGate(x,y),z)

x = -2
y =  5
z = -4
print forwardCircuit(x,y,z)