OFFSET = ord('A') - 1

def triangleNums(limit):
    """generates triangle nums <limit"""
    n = 1
    t = 1
    while t<limit:
        yield t
        n+=1
        t = .5*n*(n+1)

def wordScore(word):
    score =  map(lambda letter: ord(letter) -OFFSET, list(word))
    return sum(score)


def getWords(filename):
    words = open(filename, 'r').read()
    words = words.split(',')
    words = map(lambda x: x.strip('"'), words)
    return words



words = getWords("p042_words.txt")
scores  = map(wordScore, words)
largestTriangle = max(scores)
tris = list(triangleNums(largestTriangle))

num = 0
for score in scores:
    if score in tris:
        num+=1
print num
