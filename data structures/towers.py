
l = []
m = []
r = []

def initTowers(size):
    
    for i in xrange(size,0,-1):
        l.append(i)
    printStep()
    move(size,l, r, m)
    printStep()
    
def move(n,start,end,store):
    if n == 0:
        return
    move(n-1,start, store, end)
    end.append(start.pop())
    printStep()
    move(n-1, store, end, start)
    
    
        
def printStep():
    print l
    print m
    print r
    print


initTowers(4)
