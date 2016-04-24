#Shell sort to be improved further by using interval = interval *3 +1

def shellSort(aList):
	subList=0
	subList=len(aList)//2

	while(subList > 0):
		for startIndex in range(subList):
			gapInsertionSort(aList,startIndex,subList)
			print("After increments of size ",subList,"  The list is ",str(aList))
		subList= subList // 2


def gapInsertionSort(aList,startIndex,gap):
	for i in range(startIndex+gap,len(aList),gap):
		currentValue=aList[i]
		position=i
		while(position >=gap and aList[position - gap] > currentValue):
			aList[position]=aList[position-gap]
			position=position-gap

		aList[position]=currentValue



alist = [54,26,93,17,77,31,44,55,20]
print("initial list " + str(aList))
shellSort(alist)
print(alist)