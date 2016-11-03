arr=[10,9,8,7,6,5,4,3,2,1]
#arr=[100,50,10,5,6]

def minHeapify(arr,l,heapIndex):
	lChildIndex=heapIndex*2 +1
	rChildIndex=heapIndex*2 +2
	if(lChildIndex <=l and arr[lChildIndex] < arr[heapIndex]):
		smallest=lChildIndex
	else:
		smallest=heapIndex
	if(rChildIndex <=l and arr[rChildIndex] < arr[smallest]):
		smallest=rChildIndex
	if(smallest != heapIndex):
		arr[smallest],arr[heapIndex]=arr[heapIndex],arr[smallest]
		minHeapify(arr,l,smallest)

def maxHeap(arr,l,heapIndex):
	lChildIndex=heapIndex*2+1
	rChildIndex=heapIndex*2+2
	if(lChildIndex<=l and arr[lChildIndex] > arr[heapIndex]):
		largest=lChildIndex
	else:
		largest=heapIndex
	if(rChildIndex <=l and arr[rChildIndex] > arr[largest]):
		largest=rChildIndex
	if(largest != heapIndex):
		arr[heapIndex],arr[largest]=arr[largest],arr[heapIndex]
		maxHeap(arr,l,largest)


def buildHeapMin(arr):
	l=len(arr)
	heapIndex=(l/2) -1
	while(heapIndex>=0):
		minHeapify(arr,l-1,heapIndex)
		print("{0} arr and index {1}".format(arr,heapIndex))
		heapIndex-=1

def buildHeapMax(arr):
	l=len(arr)
	heapIndex=(l/2)-1
	while(heapIndex >=0):
		maxHeap(arr,l-1,heapIndex)
		heapIndex-=1


def heapSort(arr):
	l=len(arr)-1
	while(l>=0):
		arr[0],arr[l]=arr[l],arr[0]
		l-=1
		maxHeap(arr,l,0)

buildHeapMax(arr)
print(arr)
heapSort(arr)
print(arr)



