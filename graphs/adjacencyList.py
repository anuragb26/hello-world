class Vertex:
	def __init__(self,id):
		self.id=id
		self.connectedTo={}
		self.distance=0
		self.pred=None
		self.color='white'
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr]=weight

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

	def getId(self):
		return self.id

	def setColor(self,color):
		self.color=color

	def setPred(self,pred):
		self.pred = pred

	def setDistance(self,d):
		self.distance=d

	def getColor(self):
		return self.color

	def getPred(self):
		return self.pred

	def getDistance(self):
		return self.distance

	def __str__(self):
		return str(self.id) + " connected to " + str([x.id for x in self.connectedTo])

	def __repr__(self):
		return str(self.id) + " connected to " + str([x.id for x in self.connectedTo])

	def getConnections(self):
		return  self.connectedTo.keys()



class Graph:
	def __init__(self):
		self.numOfVertices=0
		self.vertList={}

	def addVertex(self,key):
		self.numOfVertices+=1
		newVertex=Vertex(key)
		self.vertList[key]=newVertex
		return newVertex

	def addEdge(self,f,t,cost=0):
		if(f not in self.vertList):
			nv=self.addVertex(f)
		if(t not in  self.vertList):
			nv=self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t])

	def getVertices(self):
		return self.vertList.keys()
	
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self,n):
		return n in self.vertList		

	def __str__(self):
		return str(self.vertList)

  
if __name__ == "__main__":

	v1 = Vertex("a")
	v2= Vertex("b")
	v3=Vertex("c")
	g = Graph()

	for i in range(6):
		g.addVertex(i)
	g.addEdge(0,2,10)

	print (g.getVertices())

	for vertex in g:
		print (str(vertex) +" \n")




















