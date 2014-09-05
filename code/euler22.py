OFFSET =  ord('A') -1

def mergeSort(stuff):
    size = len(stuff)
    if size <=1 :
        return stuff
    # split into left and right
    left = stuff[0:size/2]
    right = stuff[size/2:size]
    # divide
    left = mergeSort(left)
    right = mergeSort(right)

    # conquer
    return merge(left,right)


def merge(a, b):
    a.reverse()
    b.reverse()
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[-1] <= b[-1]:
            c.append(a.pop())
        else:
            c.append(b.pop())
    if len(a):
        a.reverse()
        c.extend(a)
    if len(b):
        b.reverse()
        c.extend(b) 
    return c

#test  =[5,3,7,1,6,7,30,21, 4523,23,7876,3142,2,4434,9]

def getNameScore(name,i):
    name = map(lambda letter: ord(letter) - OFFSET, list(name))
    return reduce(lambda x,y: x+y, name) *i


names = open("p022_names.txt",'r').read()


names = names.split(',')

names = map(lambda x: x.strip("\""), names) # clean out the pesky quotes
names2 = names[:]
names2.sort()

names = mergeSort(names)
 
totalScore = reduce(lambda x,y: x+y, map(getNameScore,  names, range(1,len(names)+ 1))) 
print totalScore
