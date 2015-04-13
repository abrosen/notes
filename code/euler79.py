## This is a topological ordering problem

FILE =  "p079_keylog.txt"

class Node(object):
    out = []
    incoming = []
    def __init__(self, name):
        self.name = name
    
    def add_out(self, e):
        self.out.append(e)
    
    def add_incoming(self, e):
        self.incoming.append(e)




def doTheThing():
    attempts = list(set(open(FILE, 'r').read().split()))
    
    print(attempts)
    attempts  =  list(map(lambda x:  list(str(x)), attempts))
    print(attempts)
    
    
    nums = []
    for attempt in attempts:
        for num in attempt:
            if num not in nums:
                nums.append(num)
        
    nodes = []
    
    for num in nums:
        nodes.append(Node(num))
    
    for attempt in attempts:
        pass
    
    
    ordering = []
    S = set()
    
    
    

if __name__ == '__main__':
    doTheThing()
