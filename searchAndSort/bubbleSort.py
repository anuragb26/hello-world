def bubbleSort(alist):
	for i in range(len(alist)):
		j=0
		while(j < len(alist)-1-i):
			if(alist[j]>alist[j+1]):
				alist[j],alist[j+1]=alist[j+1],alist[j]
			j+=1
		print("with i " + str(i) + " list " + str(alist))



def bubbleSortOptimum(alist):
		sorted = False
		i=0
		while i < len(alist) and not sorted:
			sorted=True
			j=0
			while(j < len(alist) - 1 - i):
				if(alist[j] > alist[j+1]):
					sorted=False
					alist[j],alist[j+1]=alist[j+1],alist[j]
				j+=1
			print("with i " + str(i) + " list " + str(alist))			
		i+=1	


#alist = [54,26,93,17,77,31,44,55,20]
alist=[20,30,40,90,50,60,70,80,100,110]
bubbleSort(alist)
print(alist)
alist=[20,30,40,90,50,60,70,80,100,110]
bubbleSortOptimum(alist)
print(alist)