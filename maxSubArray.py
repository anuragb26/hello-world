def maxSubArray(arr,k):

	i=0
	currentSum=0
	currentStartingIndex=0
	startIndex=0
	endIndex=0
	length=0
	currentLength=0
	arrayLength=len(arr)
	
	solutionDoesNotExist = True
	while i <= arrayLength:
		
		while(currentSum > k):
				currentSum = currentSum - arr[currentStartingIndex]
				currentStartingIndex+=1

		if(currentSum == k):
			solutionDoesNotExist=False
			if(currentLength > length):
				length=currentLength
				startIndex=currentStartingIndex
				endIndex=i-1
				currentLength=0
		
		if(i < arrayLength):
			currentSum = currentSum + arr[i]
			currentLength+=1
		i+=1
		

	if (not solutionDoesNotExist):
		#return [arr[startIndex],arr[endIndex]]
		return [startIndex,endIndex]

x=x=input(" Enter space seperated array elements space seperated ")
arr=list(map(int,x.split()))

print(maxSubArray(arr,55))
