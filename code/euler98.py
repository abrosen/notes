FILE = "p098_words.txt"

def buildDict(words):
	d = {}
	for word in words:
		k = "".join(sorted(word))
		if k not in d.keys():
			d[k] = []
		d[k].append(word)
	return d

def doTheThing():
	words = open(FILE).read().split(',')
	words = list(map(lambda x: x.strip('"'), words))
	d =  buildDict(words)
	print(d)


if __name__ == '__main__':
	doTheThing()