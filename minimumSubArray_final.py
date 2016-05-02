def minimumSubArrayFinal(aList):
	
	lowerEnd=-1
	upperEnd=-1
	arrayLength = len(aList)

	i=0
	j=1

	while(j<arrayLength):
		if(aList[j] < aList[i]):
			break
		else:
			j+=1
			i+=1

	if(j == arrayLength -1): 	#Reaching at the end in the first run implies that we have traversed a sorted array
		return None
	else:
		lowerEnd=i

	j=arrayLength-1
	i=j-1

	while(j>0):
		if(aList[i] > aList[j]):
			break
		else:
			j-=1
			i-=1

	upperEnd=j

	currentMax=aList[lowerEnd]
	currentMin=aList[lowerEnd]
	j=lowerEnd+1


	while(j<=upperEnd):
		if(aList[j] > currentMax):
			currentMax=aList[j]
		if(aList[j] < currentMin):
			currentMin=aList[j]
		j+=1
		

	i=0

	while(i < lowerEnd):
		if(aList[i] > currentMin): 						#Since array before lower end is sorted in increasing order we can break out at first false condition
			lowerEnd=i
			break
		i+=1
	j=arrayLength-1

	while(j > upperEnd):
		if(aList[j] < currentMax):						#Since array before upper end is sorted in decreasing order we can break out at first false condition
			upperEnd=j
			break
		j-=1

	return [lowerEnd,upperEnd]

listOne=[10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
listTwo= [0, 1, 15, 25, 6, 7, 30, 40, 50]

print(minimumSubArrayFinal(listOne))
print(minimumSubArrayFinal(listTwo))