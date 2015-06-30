from eulertools import isPrime

SINGLE_PRIMES = [2,3,5,7]


def startsWithPrime(n):
	firstDigit = int(str(n)[0])
	return firstDigit in SINGLE_PRIMES

def endsWithPrime(n):
	lastDigit = int(str(n)[0])
	return lastDigit in SINGLE_PRIMES


def isLeftTrunc(n):
	while True:
		if not isPrime(n):
			return False
		n = str(n)
		if len(n) == 1:
			return True
		n = int(n[1:])
	

def isRightTrunc(n):
	while n > 0:
		if not isPrime(n):
			return False
		n /= 10
	return True 


def isTrunc(n):
	if startsWithPrime(n) and endsWithPrime(n):
		return isLeftTrunc(n) and isRightTrunc(n)


def doTheThing():
	s = 0
	for i in range(11,1000000,2):
		if isTrunc(i):
			print(i)
			s += i
	print(s)

if __name__ == '__main__':
	doTheThing()