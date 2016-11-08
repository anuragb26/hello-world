'''
Three classes for following the adjacency list representation
1st-> node class currently only has name as member
2nd-> edge class currently has two node objects as its member
3rd -> digraph class has a dictionary key is the node and value is the list of nodes linked to that node
'''


class Node(obj):

	def __init__(self,name):
		self.name=name
	def getName(self):
		return self.name
	def __str__(self):
		return self.name