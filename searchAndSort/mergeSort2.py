#!/usr/env/bin python3




arr = [54,26,93,17,77,31,44,55,20]



def mergeSort(arr,start,end):
	if(start < end):
		mid=(start+end)/2
		lArr=mergeSort(arr,start,mid)
		rArr=mergeSort(arr,mid+1,end)
		print("{0} and {1}".format(start+1,end+1))
		return merge(lArr,rArr)
	else:
		return [arr[start]]
		#print("{0} in else".format(arr[start]))
		#l=[]
		#l.append(arr[start])
		#return l

def merge(lArr,rArr):
	leftLen=len(lArr)
	rightLen=len(rArr)
	print("{0} and {1} in merge".format(lArr,rArr))
	totalLen=leftLen + rightLen
	arrCopy=[None]*(totalLen)
	i,j,k=0,0,0
	while(i<leftLen and j < rightLen):
		if(lArr[i] <= rArr[j]):
			arrCopy[k]=lArr[i]
			i+=1
		else:
			arrCopy[k]=rArr[j]
			j+=1
		k+=1
	if(i < leftLen):
		while(i < leftLen):
			arrCopy[k]=lArr[i]
			k+=1
			i+=1
	if(j < rightLen):
		while(j < rightLen):
			arrCopy[k]=rArr[j]
			k+=1
			j+=1
	print("arraycopy is {0}".format(arrCopy))		
	return arrCopy

print("array is {0}".format(arr))
arrC=mergeSort(arr,0,len(arr)-1)
print (arrC)
