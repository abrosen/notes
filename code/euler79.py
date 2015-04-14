## This is a topological ordering problem

FILE =  "p079_keylog.txt"

class Node(object):
    def __init__(self, name):
        self.name = name
        self.outs = []
        self.ins = []
    
    
    def add_out(self, e):
        if e not in self.outs:
            self.outs.append(e)
    
    def add_in(self, e):
        if e not in self.ins:
            self.ins.append(e)

def createTheNodes(attempts):
    nums = []
    for attempt in attempts:
        for num in attempt:
            num = int(num)
            if num not in nums:
                nums.append(num)
        
    nodes = {}
    for num in nums:
        nodes[num] = Node(num)
    
    print(nodes)
        
    for attempt in attempts:
        a = int(attempt[0])
        b = int(attempt[1])
        c = int(attempt[2])
        # add edge 1
        print(a,b)
        nodes[a].add_out(b)
        nodes[b].add_in(a)

        # add edge 2
        nodes[b].add_out(c)
        nodes[c].add_in(b)
        
        
    for i in nodes:
        print(i, nodes[i].ins)
    return nodes


def doTheThing():
    # stupid quick-to-write hack
    # reading in the text file, each line (attempt) as an element
    attempts = list(set(open(FILE, 'r').read().split()))
    #now I split each attempt into a list of individual key presss
    attempts  =  list(map(lambda x:  list(str(x)), attempts))
   
    
    nodes = createTheNodes(attempts)

    ordering = []
    S = []
    for n in nodes.values():
        if len(n.ins) == 0:

            S.append(n)
    while(len(S)):
        n =  S.pop()
        ordering.append(n.name)
        for m in n.outs:
            print m
            nodes[m].ins.remove(n.name)
            if len(nodes[m].ins) == 0:
                S.append(nodes[m])
    print ordering

    
    
    

if __name__ == '__main__':
    doTheThing()
