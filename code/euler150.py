import copy
test = [
[15],
[-14,-7],
[20,-13,-5],
[-3,8,23,-26],
[1,-4,-5,-18,5],
[-16,31,2,9,28,3]
]
def randomGenerator():
    """generates psuedorandom numbers using Linear Congruential Generator"""
    t = 0
    while True:
        t = (615949*t +797807) % 2**20
        yield t-2**19

def createTriangle(n):
    """creates a triangle of n random integers"""    
    triangle = []
    rand = randomGenerator()
    rowLength = 1
    i = 0
    while i<n:
        row = []
        for j in xrange(rowLength):
            row.append(next(rand))
            i+=1
        triangle.append(row)
        rowLength+=1
    return triangle 

def generateCheatSheet(triangle):
    cheatSheet =  copy.deepcopy(triangle[:])
    for ithRow in xrange(len(triangle)):
        #print ithRow
        for jthNum in xrange(1,len(triangle[ithRow])):
            cheatSheet[ithRow][jthNum] += cheatSheet[ithRow][jthNum-1]
    return cheatSheet



def findSmallestSubtriangle(triangle):
    best = 20
    lookupTable = generateCheatSheet(triangle)
    for ithRow in xrange(len(triangle)):
        print ithRow
        for jthNum in xrange(len(triangle[ithRow])):
            for depth in xrange(1,len(triangle) - ithRow):
                if jthNum == 0:
                    triangle[ithRow][jthNum] += lookupTable[ithRow+depth][jthNum+depth] 
                else:
                    triangle[ithRow][jthNum] += lookupTable[ithRow+depth][jthNum+depth] - lookupTable[ithRow+depth][jthNum-1] 
                if triangle[ithRow][jthNum] < best:
                    best = triangle[ithRow][jthNum]
                    print best
    return best


if __name__ == '__main__':
    triangle = createTriangle(500500)
    print findSmallestSubtriangle(test)
    