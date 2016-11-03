import sys

arr=[6,2,7,14,3,12,9,4,8,10]
arrCopy=arr[:]


def maxHeapify(i,arr,N):
	lChildIndex=2*i + 1
	rChildIndex=2*i + 2
	maxIndex=i
	if lChildIndex<N and arr[maxIndex] < arr[lChildIndex]:
		maxIndex=lChildIndex
	if rChildIndex<N and arr[maxIndex] < arr[rChildIndex]:
		maxIndex=rChildIndex
	if maxIndex != i:
		arr[maxIndex],arr[i]=arr[i],arr[maxIndex]
		maxHeapify(maxIndex,arr,N)

def buildHeap(arr):
	N=len(arr)
	i=N//2
	while(i>=0):
		maxHeapify(i,arr,N)
		i-=1


def heapSort(arr):
	buildHeap(arr)
	print(arr)
	N=len(arr)
	heapSize=N-1
	while(heapSize >= 0):
		arr[0],arr[heapSize]=arr[heapSize],arr[0]
		#print("{} and {}".format(arr[heapSize-1],arr))
		maxHeapify(0,arr,heapSize)
		heapSize-=1

def increaseKey(arr,index,value):
	if(value < arr[index]):
		raise ValueError("Value to be inserted should be higher than {0}".format(arr[index]))

	arr[index]=value

	while(index >=0 and arr[(index-1)//2] < arr[index]):
		arr[index],arr[(index-1)//2]=arr[(index-1)//2],arr[index]
		index=(index-1)//2

def insertKey(arr,value):
	arr.append(-1*sys.maxsize)
	increaseKey(arr,len(arr)-1,value)


buildHeap(arrCopy)
#insertKey(arrCopy,13)
print(arrCopy)
