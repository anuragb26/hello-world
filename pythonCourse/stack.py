class Stack(obj):
	def __init__(self):
		self.arr=[]
	def push(self,node):
		self.arr.push(node)
	def pop(self):
		if len(arr)==0:
			raise ValueError("Stack is empty")
		else:
			return self.arr.pop()
	def isEmpty(self):
		empty=False
		if(len(arr)==0):
			empty=True
		return empty
	def size(self):
		return len(arr)