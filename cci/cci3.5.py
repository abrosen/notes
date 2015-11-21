class StackQueue():
	def __init__(self):
		self.s1 = []
		self.s2 = []
	
	def enqueue(self, item):
		self.s1.append(item)

	def dequeue(self):
		if len(self.s1) == 0:
			return None
		while len(self.s1) != 0:
			self.s2.append(self.s1.pop())
		retval = self.s2.pop()
		while len(self.s2) != 0:
			self.s1.append(self.s2.pop())
		return retval


q =  StackQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
