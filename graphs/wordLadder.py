
from adjacencyList import Vertex
from adjacencyList import Graph
from queue import Queue

def buildGraph(wordFile):
	g=Graph()
	wordMap={}

	wordList=open(wordFile)
	words=wordList.read().split()

	for word in words:
		#print(" word is " + word)
		for i in range(len(word)):
			bucket=word[:i]+"_"+word[i+1:]
			if(bucket in wordMap):
				wordMap[bucket].append(word)
			else:
				wordMap[bucket]=[word]
	for bucket in wordMap:
		for word1 in wordMap[bucket]:
			for word2 in wordMap[bucket]:
				if word1 != word2:
					g.addEdge(word1,word2)
	#return g.getVertex("sage")	
	return g			


def bfs(g,startVertex):
	startVertex.setDistance(0)
	startVertex.setPred(None)
	vertexQueue=Queue()
	vertexQueue.enqueue(startVertex)
	while(vertexQueue.size() > 0):
		currentVertex=vertexQueue.dequeue()
		for nbr in currentVertex.getConnections():
			if(nbr.getColor()=="white"):
				nbr.setColor("grey")
				nbr.setDistance(currentVertex.getDistance()+1)
				nbr.setPred(currentVertex)
				vertexQueue.enqueue(nbr)

		currentVertex.setColor("black")

		
def traverse(vert):
	vert2=vert
	while(vert2.getPred()):
		print(vert2.getId())
		vert2=vert2.getPred()
	print(vert2.getId())

wordFile="words.txt"
#print(buildGraph(wordFile))
g=buildGraph(wordFile)

bfs(g,g.getVertex("fool"))

print(g.getVertex("sage").getDistance())

print(traverse(g.getVertex("sage")))
