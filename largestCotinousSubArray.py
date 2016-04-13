def lcs(arr):

	currentMax=arr[0]
	maxSum=arr[0]

	for num in arr[1:]:
		currentMax=max(num,num+currentMax) # at this point you are deciding whether the number can be used to start a new sub array 
		maxSum=max(maxSum,currentMax)

	return maxSum

print lcs([-2, -3, 4, -1, -2, 1, 5, -3])