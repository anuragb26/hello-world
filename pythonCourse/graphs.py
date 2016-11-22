'''
Three classes for following the adjacency list representation
1st-> node class currently only has name as member
2nd-> edge class currently has two node objects as its member
3rd -> digraph class has a dictionary key is the node and value is the list of nodes linked to that node
'''

class Stack(object):
	def __init__(self):
		self.arr=[]
	def push(self,node):
		self.arr.append(node)
	def pop(self):
		if len(self.arr)==0:
			raise ValueError("Stack is empty")
		else:
			return self.arr.pop()
	def isEmpty(self):
		empty=False
		if(len(self.arr)==0):
			empty=True
		return empty
	def size(self):
		return len(self.arr)
	def inStack(self,node):
		present=False
		if node in self.arr:
			present=True
		return present

class Node(object):

	def __init__(self,name):
		self.name=name
	def getName(self):
		return self.name
	def __str__(self):
		return self.name

class Edge(object):

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
		return self.src.getName() + "-->" + self.dest.getName()





class Digraph():

	def __init__(self):
		self.edges={}

	def addNode(self,node):
		if not isinstance(node,Node):
			raise TypeError("Please provide an instance of Node class to add in the Graph")
		if node in self.edges:
			raise ValueError("Node already exists in the Graph")
		self.edges[node]=[]

	def addEdge(self,edge):
		if not(edge.getSource() in self.edges and edge.getDestination() in self.edges):
			raise ValueError('Edge not in graph')
		else:
			self.edges[edge.getSource()].append(edge.getDestination())
	def connectedTo(self,node):
		return self.edges[node]

	def hasNode(self,node):
		return node in self.edges

	def getNode(self,name):
		for node in self.edges:
			if name == node.getName():
				return node
		raise NameError("No such Node Exists") 

	def getVertices(self):
		return Object.keys(self.edges)

	def __str__(self):
		result=''
		for src in self.edges:
			for dest in self.edges[src]:
				result+= src.getName() + "->" + dest.getName()
				result+='\n'
		return result[:-1]


class Graph(Digraph):

	def addEdge(self,edge):
		Digraph.addEdge(self,edge)
		rev=Edge(edge.getDestination(),edge.getSource())
		Digraph.addEdge(self,rev)


def buildCityGraph(graphType):
	g=graphType()
	for name in ('Boston', 'Providence', 'New York', 'Chicago',
				'Denver', 'Phoenix', 'Los Angeles'):
		g.addNode(Node(name))
	g.addEdge(Edge(g.getNode('Boston'),g.getNode('Providence')))
	g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
	g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
	g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
	g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
	g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
	g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
	g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
	g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
	g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))


	return g

#print (buildCityGraph(Digraph))

def printPath(path):
	result=''

	for i in range(len(path)):
		result+= str(path[i])
		if(i!=len(path)-1):
			result+="->"
	return result

def depthFirstSearch(graph,node,path=[]):
	
	path=path+[node]
	#print(printPath(path))
	for vertex in graph.connectedTo(node):
		if(vertex not in path):
			path=depthFirstSearch(graph,vertex,path)
	#print(printPath(path))
	return path

def spath(graph,start,end,path,shortest):

	path = path + [start]
	if(start==end):
		return path	
	for vertex in graph.connectedTo(start):
		print("inside " + str(start) +   " vertex " + str(vertex) + " and path " + printPath(path))
		if(vertex not in path):
			if shortest == None or len(path) < len(shortest):
				print("calling sPath for " + str(vertex))
				newPath=spath(graph,vertex,end,path,shortest)
				if newPath!=None:
					shortest=newPath
	return shortest


def finalDfs(graph,start,end,path):
	path = path + [start]
	#if start==end:
		#return path
	for node in graph.connectedTo(start):
		if node not in path:
			finalDfs(graph,node,end,path)
	return path
		



g=buildCityGraph(Digraph)
p=depthFirstSearch(g,g.getNode("Boston"),[])
printPath(p)









