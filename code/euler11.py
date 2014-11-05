def loadGrid(filename):
    nums = []
    numfile =  open(filename)
    for line in numfile:
        line = line.split()
        line = map(int, line)
        nums.append(line)
    return nums

def searchHorizontal(grid, size = 4):
    numCols = len(grid[0])
    numRows =  len(grid)
    best = -50
    for i in xrange(numRows):
        for j in xrange(numCols - size):
            product =  grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if product > best:
                best =  product
    return best       


def searchVertical(grid, size = 4):
    numCols = len(grid[0])
    numRows =  len(grid)
    best = -50
    for i in xrange(numRows - size):
        for j in xrange(numCols):
            product =  grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if product > best:
                best =  product
    return best 


def searchDiagonalUp(grid, size = 4):
    numCols = len(grid[0])
    numRows =  len(grid)
    best = -50
    for i in xrange(size-1, numRows):
        for j in xrange(numCols-size):
            product =  grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if product > best:
                best =  product
    return best 


def searchDiagonalDown(grid, size = 4):
    numCols = len(grid[0])
    numRows =  len(grid)
    best = -50
    for i in xrange(numRows-size):
        for j in xrange(numCols-size):
            product =  grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if product > best:
                best =  product
    return best 


grid = loadGrid("nums11")
for row in grid:
    print row

print  len(grid[0])
print  len(grid)
print searchHorizontal(grid)
print searchVertical(grid)
print searchDiagonalUp(grid)
print searchDiagonalDown(grid)