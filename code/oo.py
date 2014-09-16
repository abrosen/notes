class Node(object):
    __i = 12345

    def say_hello(self):
       print "hello"

x = Node()
print x.__i
x.say_hello()