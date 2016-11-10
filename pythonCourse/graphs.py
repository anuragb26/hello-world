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

class Edge(obj):

	def __init__(self,src,dest):
		if(not isinstance(src,Node)):
			raise ValueError("Please provide an instance of Node Class for source")
		if(not isinstance(dest,Node)):
			raise ValueError("Please provide an instance of Node Class for destination")
		self.src=src
		self.dest=dest

	def getSource(self):
		return self.src

	def getDestination(self):
		return self.dest

	def __str__(self):
		return self.src.getName() + "-->" self.dest.getName()



class Digraph():

	def __init__(self):
		self.edges={}

	def addNode(self,node):
		if not isinstance(node,Node):
			raise TypeError("Please provide an instance of Node class to add in the Graph")
		if node in self.edges:
			raise ValueError("Node already exists in the Graph")
		self.edges[node]=[]

	def addEdge(self,src,dest):
	def connectedTo(self,node):
		return self.edges[node]

	def hasNode(self,node):
		return node in self.edges

	def getNode(self,name):
		for node in self.edges:
			if name == self.edges[node].getName():
				return node
		raise NameError("No such Node Exists") 