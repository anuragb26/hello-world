def selectionSort(alist):
	i=0
	while(i < len(alist)):
		minIndex=i
		j=i+1
		while(j<len(alist)):
			if(alist[j] < alist[minIndex]):
				minIndex=j
			j+=1
		alist[i],alist[minIndex]=alist[minIndex],alist[i]
		print("with i " + str(i) + " list " + str(alist))
		i+=1


alist = [54,26,93,17,77,31,44,55,20]
print(" before " + str(alist))
selectionSort(alist)
print(alist)