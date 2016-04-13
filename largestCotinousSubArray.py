def lcs(arr):

	currentMax=arr[0]
	maxSum=arr[0]

	for num in arr[1:]:
		print " in with " + str(num)
		currentMax=max(num,num+currentMax) # at this point you are deciding whether the number can be used to start a new sub array 
		print "currentMax is "+ str(currentMax)
		maxSum=max(maxSum,currentMax)
		print "maxSum is "+ str(maxSum)

	return maxSum

print lcs([-2, -3, 4, -1, -2, 1, 5, -3])