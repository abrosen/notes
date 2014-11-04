import random
def forwardMultiplyGate(x,y):
	return x*y


x = -2
y =  3
out =  forwardMultiplyGate(x,y)
h = 0.00000001


f =  forwardMultiplyGate
x_derv = (f(x+h,y) - f(x,y))/h
y_derv = (f(x,y+h)- f(x,y))/h

print x_derv, y_derv