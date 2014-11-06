#n squares = n+1 points
# The N is for determining how many squares there are in the graph
# our paths travel along the corners
N = 20

def calcRoutes(grid):
    """
    This is a straightforward dynamic programming problem.
    The number of paths from point x to the bottom-right is equal to 
    the number of paths starting from the point right plus
    the number of paths starting from the point down
    eg grid[i][j] =  grid[i+1][j] + grid[i][j+1]

    All the points along the bottom and right edges have only one path
    """
    lenRows = len(grid[0])
    lenCols = len(grid)
    for i in xrange(lenRows-2,-1,-1):
        for j in xrange(lenCols-2,-1,-1):
            grid[i][j] =  grid[i+1][j] + grid[i][j+1]
    return grid

if __name__ == '__main__':
    grid =  [ [1 for x in xrange(N+1)] for x in xrange(N+1)]
    grid = calcRoutes(grid)
    for line in grid:
        print line
    print "There are ", grid[0][0], "right down paths"

