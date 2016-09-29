arr = [54,26,93,17,77,31,44,55,20]


def partition(arr,start,end):
	pivot=arr[end]
	pivotIndex=start-1
	currentIndex=start
	while(currentIndex < end):
		if(arr[currentIndex] < pivot):
			pivotIndex+=1
			arr[pivotIndex],arr[currentIndex]=arr[currentIndex],arr[pivotIndex]
		currentIndex+=1
	pivotIndex+=1
	arr[pivotIndex],arr[end]=arr[end],arr[pivotIndex]
	print (" arr after partition {0}".format(arr))
	return pivotIndex

def quickSort(arr,start,end):
	if(start < end):
		pivot=partition(arr,start,end)
		quickSort(arr,start,pivot-1)
		quickSort(arr,pivot +1,end)



quickSort(arr,0,len(arr)-1)
print(arr)