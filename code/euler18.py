FILE = "nums18"

def loadTriangle(filename):
    triFile = open(filename)
    triangle = []
    for line in triFile:
        line = map(int,line.split())
        triangle.append(line)
    return triangle

def findOptimalRoute(triangle):
    for ithRow in xrange(len(triangle)-2, -1, -1):
        for jthNum in xrange(len(triangle[ithRow])):
            triangle[ithRow][jthNum] +=  max((triangle[ithRow+1][jthNum],triangle[ithRow+1][jthNum+1]))
    return triangle[0][0]

if __name__ == '__main__':
    triangle = loadTriangle(FILE)
    print findOptimalRoute(triangle)