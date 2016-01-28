class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Node(object):
    def __init__(self,name):
        self.name = name
        self.edges = {}

    def addEdge(self,otherNode, distance = 1):
        self.edges[otherNode] = distance

    def __str__(self):
        return self.name

class Graph(object):
    def __init__(self):
        self.nodes = {}

    def addNode(self, node):
        self.nodes[node] = {}

    def addNodes(self, nodes):
        for n in nodes:
            self.addNode(n)

    def addEdge(self, a, b, distance = 1):
        self.nodes[a][b] = distance
        self.nodes[b][a] = distance

    def addDirectedEdge(self, a, b, distance = 1):
        self.nodes[a][b] = distance

    def getNode(self, identifier):
        return self.nodes[identifier]



def dfs(root,visited = None):
    if visited is None:
        visited = {}
    visited[root] = 1
    print(root)
    for neighbor in root.keys():
        if neighbor in visited:
            dfs(neighbor,visited)





g = Graph() 
g.addNodes([1,2,3,4,5,6,7])
g.addEdge(1,2)
g.addEdge(3,4)
g.addEdge(4,3)
g.addEdge(4,6)
print(g.getNode(1))

dfs(g.getNode(1))