class Heap:

	def __init__(self,maxHeapSize):
		self.maxHeapSize=maxHeapSize
		self.heapSize=0
		self.heapArr=list()


	def buildHeapFromArr(self,arr):
		self.heapSize=len(arr)
		self.heapArr=arr
		currIndex=(self.heapSize)//2
		while(currIndex>=0):
			self.heapify(currIndex)
			currIndex-=1

	def getTop(self):
		return self.heapArr[0]

	def getHeapSize(self):
		return self.heapSize

class MaxHeap(Heap):

	def __init__(self,maxHeapSize):
		Heap.__init__(self,maxHeapSize)


	def heapify(self,currIndex):
		leftChildIndex=currIndex*2 + 1
		rightChildIndex=currIndex*2 + 2
		largestIndex=currIndex
		if(leftChildIndex < self.heapSize and self.heapArr[leftChildIndex] > self.heapArr[largestIndex]):
			largestIndex=leftChildIndex
		if(rightChildIndex < self.heapSize and self.heapArr[rightChildIndex] > self.heapArr[largestIndex]):
			largestIndex=rightChildIndex
		if(largestIndex != currIndex):
			self.heapArr[largestIndex],self.heapArr[currIndex]=self.heapArr[currIndex],self.heapArr[largestIndex]
			self.heapify(largestIndex)

	def increaseKey(self,index,value):
		if(value < self.heapArr[index]):
			raise ValueError("Wrong value for increase Key in MaxHeap")
		self.heapArr[index]=value
		while(index >0 and self.heapArr[(index-1)//2] < self.heapArr[index]):
			self.heapArr[(index -1)//2],self.heapArr[index]=self.heapArr[index],self.heapArr[(index-1)//2]
			index=(index-1)//2

	def insert(self,value):
		self.heapSize+=1
		self.heapArr.append(value)
		self.increaseKey(self.heapSize-1,value)

	def extractMax(self):
		if(not self.heapSize):
			raise ValueError('Cannot Extract element from empty maxHeap')
		val=self.heapArr[0]
		self.heapArr[0]=self.heapArr[self.heapSize-1]
		self.heapArr.pop()
		self.heapSize=self.heapSize-1
		self.heapify(0)
		return val




class MinHeap(Heap):

	def __init__(self,maxHeapSize):
		Heap.__init__(self,maxHeapSize)

		
	def heapify(self,currIndex):
		leftChildIndex=currIndex*2 + 1
		rightChildIndex=currIndex*2 + 2
		smallestIndex=currIndex
		if(leftChildIndex < self.heapSize and self.heapArr[leftChildIndex] < self.heapArr[smallestIndex]):
			smallestIndex=leftChildIndex
		if(rightChildIndex < self.heapSize and self.heapArr[rightChildIndex] < self.heapArr[smallestIndex]):
			smallestIndex=rightChildIndex
		if(smallestIndex != currIndex):
			self.heapArr[smallestIndex],self.heapArr[currIndex]=self.heapArr[currIndex],self.heapArr[smallestIndex]
			self.heapify(smallestIndex)

	def decreaseKey(self,index,value):
		if(value > self.heapArr[index]):
			raise ValueError("Value is less for inserting in minHeap")
		self.heapArr[index]=value

		while(index >0 and self.heapArr[(index-1)//2] > self.heapArr[index]):
			self.heapArr[index],self.heapArr[(index-1)//2]=self.heapArr[(index-1)//2],self.heapArr[index]
			index=(index-1)//2


	def insert(self,value):
		self.heapSize+=1
		self.heapArr.append(value)
		self.decreaseKey(self.heapSize-1,value)


	def extractMin(self):
		if not self.heapArr:
			raise ValueError("Cannot extractMin from empty heap")
		val=self.heapArr[0]
		self.heapArr[0]=self.heapArr[self.heapSize-1]
		self.heapArr.pop()
		self.heapSize-=1
		self.heapify(0)
		return val


arr=[10,9,8,7,6,5,4,3,2,1]
#arr=[1,2,3,4,5]



N=len(arr)

if(N%2==0):
	heapSize=N//2
else:
	heapSize=(N+1)//2

median=0
minH=MinHeap(heapSize)
maxH=MaxHeap(heapSize)

for num in arr:
	minHeapSize=minH.getHeapSize()
	maxHeapSize=maxH.getHeapSize()
	if(minHeapSize==maxHeapSize):
		if(num < median):
			maxH.insert(num)
			median=maxH.getTop()
		else:
			minH.insert(num)
			median=minH.getTop()
	
	elif(maxHeapSize < minHeapSize):
		if(num < median):
			maxH.insert(num)
		else:
			val=minH.extractMin()
			minH.insert(num)
			maxH.insert(val)
		median=(minH.getTop()+maxH.getTop())//2
	else:
		if(num < median):
			val=maxH.extractMax()
			maxH.insert(num)
			minH.insert(val)
		else:
			minH.insert(num)
		median=(minH.getTop() + maxH.getTop())//2

print(median)








		












