import networkx as nx
from collections import deque



class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def isTreeBalanced():
    pass


def isTreeBST(root):
    if root.left is None and root.right is None:
        return True
    if root.left is None or root.left.val <=  root.val:
        if root.right is None or root.right.val > root.val:
            return isTreeBST(root.left ) and isTreeBST(root.right)
    return False
        

    
def dfs(graph,root,visited = None):
    if visited is None:
        visited = set()
    visited.add(root)
    process(root)
    for neighbor in graph[root]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)



def bfs(graph,root,visited = None):
    if visited is None:
        visited = set()
    q = deque([])
    q.append(root)
    while len(q):
        current = q.popleft()
        if current not in visited:
            process(current)
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    q.append(neighbor)
        print(q)


def dijkstra(graph, root):
    dist = {}
    prev = {}
    unvisited = set()
    
    for node in graph.nodes():
        dist[node] = float('inf')
        unvisited.add(node)
    dist[root] = 0
    current = None
    closest = root
    
    while len(unvisited):
        current = closest
        closest = None
        unvisited.remove(current)

        for neighbor in graph[current]:
            if neighbor in unvisited:
                alt = dist[current] + graph[current][neighbor]['weight']
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current
                if closest is None:
                    closest = neighbor
                elif alt < dist[closest]:
                    closest = neighbor
    return dist, prev

def bellmanFord(graph, root):
    dist = {}
    pred = {}
    for node in graph.nodes():
        dist[node] = float('inf')
    dist[root] = 0
    
    for i in range(0, len(graph.nodes())):
        for u, v in graph.edges():
            if dist[u] + graph[u][v]['weight'] < dist[v]:
                dist[v] = dist[u] + graph[u][v]['weight']
                pred[v] = u
            
            if dist[v] + graph[v][u]['weight'] < dist[u]:
                dist[u] = dist[v] + graph[v][u]['weight']
                pred[u] = v
            

    for u, v in graph.edges():
        if dist[u] + graph[u][v]['weight'] < dist[v]:
            raise Exception("Negative Cycle") 
    return dist, pred


def isRoute(graph, u, v):
    visited = set()
    q = deque([])
    q.append(u)
    while len(q):
        current = q.popleft()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            elif neighbor == v:
                    return True
            else:
                q.append(neighbor)
    return False 

def process(foo):
    print(foo)


g = nx.Graph()
# g.add_nodes_from([1,2,3,4,5,5,6,7])
g.add_edge(1, 2, weight=7)
g.add_edge(1, 3, weight=9)
g.add_edge(1, 6, weight=14)
g.add_edge(2, 3, weight=10)
g.add_edge(2, 4, weight=15)
g.add_edge(3, 4, weight=11)
g.add_edge(3, 6, weight=2)
g.add_edge(4, 5, weight=6)
g.add_edge(5, 6, weight=9)
print(bellmanFord(g,1))