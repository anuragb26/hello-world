def minimumSubArray(aList):

	lowerEnd=-1
	upperEnd=-1
	arrayLength=len(aList)
	i=0
	j=1
	while j<arrayLength:
		if(aList[j] < aList[i]):
			break
		else:
			j+=1
			i+=1
			
	lowerEnd=i

	i=arrayLength-1
	j=i-1
	
	while(j>0):
		if(aList[j] > aList[i]):
			break
		else:
			j-=1
			i-=1
	upperEnd=i
	currentMinIndex=lowerEnd
	currentMaxIndex=upperEnd

	i=lowerEnd+1
	j=upperEnd-1

	while(i<=upperEnd):
		if(aList[i] < aList[currentMinIndex]):
			currentMinIndex=i
		i+=1
	while(j>=lowerEnd):
		if(aList[j] > aList[currentMaxIndex]):
			currentMaxIndex=j
		j-=1

	i=0
	while(i <lowerEnd):
		if(aList[i] > aList[currentMinIndex]):
			currentMinIndex=i
		i+=1
	j=arrayLength-1
	while(j > upperEnd):
		if(aList[j] < aList[currentMaxIndex]):
			currentMaxIndex=j
		j-=1
	if(currentMinIndex < lowerEnd):
		lowerEnd=currentMinIndex
	if(currentMaxIndex > upperEnd):
		upperEnd=currentMaxIndex
	return [lowerEnd,upperEnd]
	#return aList

listOne=[10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
listTwo= [0, 1, 15, 25, 6, 7, 30, 40, 50]




print(minimumSubArray(listOne))
print(minimumSubArray(listTwo))

#10 12 20 25 30 31 32 35 40 50 60


#[0, 1, 15, 25, 6, 7, 30, 40, 50

#0 1 2 3 4 5 
