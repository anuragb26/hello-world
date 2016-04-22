
from adjacencyList import Vertex
from adjacencyList import Graph




class DFS(Graph):

	def __init__(self):
		super().__init__()
		self.time=0
		self.path=[]

	def dfs(self):
		for v in self:
			v.setColor('white')
			v.setPred(-1)
		for v in self:
			if v.getColor() == 'white':
				self.dfsVisit(v)					#since it is not necessary that one vertex will visit all vertexes 

	def dfsVisit(self,startVertex):
		self.time+=1
		self.path.append(startVertex.id)
		startVertex.setDiscovery(self.time)
		startVertex.setColor('grey')
		for nbr in startVertex.getConnections():
			if(nbr.getColor()=="white"):
				nbr.setPred(startVertex)
				self.dfsVisit(nbr)
		startVertex.setColor('black')
		self.time+=1
		startVertex.setFinish(self.time)

	def spath(self,startVertex,endVertex):
		if(startVertex==endVertex):
			return self.path
		else:
			self.path.append(startVertex.id)
			startVertex.setColor('grey')	
			for nbr in startVertex.getConnections():
				if (nbr.getColor == 'white'):
					self.spath(nbr)
			startVertex.setColor('black')		


g=Graph()

g.addEdge("A","B")
g.addEdge("A","D")
g.addEdge("B","D")
g.addEdge("D","E")
g.addEdge("E","B")
g.addEdge("E","F")
g.addEdge("F","C")
g.addEdge("B","C")



g1 = DFS()
g1.addEdge("A","B")
g1.addEdge("A","D")
g1.addEdge("B","D")
g1.addEdge("D","E")
g1.addEdge("E","B")
g1.addEdge("E","F")
g1.addEdge("F","C")
g1.addEdge("B","C")

g1.dfs()
print(g1.getVertex("A").getFinish())
print(g1.path)





