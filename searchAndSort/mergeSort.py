def mergeSort(arrList,low,high):
	
	if(low < high):
		mid=(low+high)//2
		mergeSort(arrList,low,mid)
		mergeSort(arrList,mid+1,high)

		i=low
		j=mid+1
		k=0
		sortedArray=[0]*(high-low+1)
		while(i <= mid and j <= high):
			if(arrList[i] < arrList[j]):
				sortedArray[k]=arrList[i]
				i+=1
				k+=1
			else:
				sortedArray[k]=arrList[j]
				j+=1
				k+=1

		while(i <= mid):
			sortedArray[k]+=arrList[i]
			k+=1
			i+=1
		while(j <= high):
			sortedArray[k]=arrList[j]
			k+=1
			j+=1

		a=0
		while(low <=high):
			arrList[low]=sortedArray[a]
			low+=1
			a+=1





alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist,0,len(alist)-1)
print(alist)



