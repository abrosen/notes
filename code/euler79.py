## This is a topological ordering problem

FILE =  "p079_keylog.txt"

class Node(object):
    self.out = []
    self.incoming = []
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
    
    
    nodes = set()
    ordering = []
    S = set()
    
    
    

if __name__ == '__main__':
    doTheThing()
