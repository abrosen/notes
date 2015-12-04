
class Node(object):
    def __init__(self,data = None,next_node= None):
        self.data = data
        self.next_node = next_node
        

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
        
    def insert(self,node):
        curr  = self.head
        if self.head is None:
            self.head =  node
        else:
            while curr.next_node is not None:
                curr = curr.next_node
            curr.next_node = node
    
    def delete(self, data):
        curr = self.head
        
        if curr.data == data:
            self.head =  self.head.next_node
        
        
        while curr.next_node is not None:
            if curr.next_node.data == data:
                curr.next_node = curr.next_node.next_node
                return
            else:
                curr =  curr.next_node
    
    def insertString(self,string):
        for c in string:
            n = Node(c)
            self.insert(n)
    
    def __str__(self):
        out = ""
        if self.head is None:
            return out
        
        curr = self.head
        out += curr.data
        while curr.next_node is not None:
            curr =  curr.next_node
            out += curr.data
        return out

    def delete_dups(self):
        curr  = self.head
        table =  {}
        table[curr.data] =  1
        while curr.next_node is not None: 
            if curr.next_node.data in table:
                curr.next_node =  curr.next_node.next_node
            else:
                table[curr.next_node.data] = 1
            curr  = curr.next_node 
            
        

L = LinkedList()
L.insertString("Follow Up")
L.delete_dups()
print(L)
