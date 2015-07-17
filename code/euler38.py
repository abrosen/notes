PAN_SET = set(list("123456789"))

def pandigitalMult(x):
	ans = ""
	n = 1
	while True:
		ans =  ans + str(x*n)
		checker =  set(list(ans))
		if checker == PAN_SET:
			return int(ans)
		if len(ans) != len(checker):
			return 0
		n = n+1


def test():
	best = 918273645
	for x in range(9000,9999):
		ans = pandigitalMult(x)
		if ans == 0:
			continue
		else:
			print ans
		

def doTheThing():
	test()

if __name__ == '__main__':
	doTheThing()