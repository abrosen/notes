FILE = "p098_words.txt"

def buildDict(words):
	d = {}
	for word in words:
		k = "".join(sorted(word))
		if k not in d.keys():
			d[k] = []
		d[k].append(word)
	return d

def isSquare():
	pass

	
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
