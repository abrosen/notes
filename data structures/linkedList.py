
class Node(object):
    def __init__(self, data):
        self.nextNode = None
        self.data =  data
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    
    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head =  node
        else:
            current =  self.head
            while current.nextNode is not None:
                current = current.nextNode
            current.nextNode =  node
            
    def addAtIndex(self, data, i):
        node = Node(data)
        if i == 0:
            node.nextNode =  self.head
            self.head = node
            return
        currIndex = 0
        curr =  self.head
        while currIndex < i -1 and curr.nextNode is not None:
            curr =  curr.nextNode
            currIndex += 1
        node.nextNode =  curr.nextNode
        curr.nextNode = node
        
        
            
    def delete(self,data):
        current =  self.head
        if current is None:
            return False
        if current.data == data:
            self.head = current.nextNode
        else:
            while current.nextNode is not None:
                if current.nextNode.data ==  data:
                    current.nextNode =  current.nextNode.nextNode
                    return True
                current = current.nextNode
            return False
        
        
    def printContents(self):
        current =  self.head
        if current is None:
            print "[]"
        print current.data
        while current.nextNode is not None:
            print current.nextNode.data
            current =  current.nextNode
        
    
l =  LinkedList()
l.add(1)
l.add(2)
l.add(-50)
l.add(54234)
l.add(0)
l.add(34527)
l.printContents()
l.delete(1)
print
l.printContents()

l.delete(34527)
print
l.printContents()


l.delete(54234)
print
l.printContents()


l.addAtIndex(0,0)
print
l.printContents()

l.addAtIndex(1,1)
print
l.printContents()

l.addAtIndex(12,4)
print
l.printContents()




