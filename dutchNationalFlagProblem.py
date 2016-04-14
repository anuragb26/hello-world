def dnf(arr):
	firstIndex=0
	secondIndex=0
	thirdIndex=len(arr)-1
	while(secondIndex <= thirdIndex):
		if(arr[secondIndex]==5):
			arr[secondIndex],arr[firstIndex]=arr[firstIndex],arr[secondIndex]
			secondIndex+=1
			firstIndex+=1
		elif(arr[secondIndex]==6):
			secondIndex+=1
		elif(arr[secondIndex]==7):
			arr[secondIndex],arr[thirdIndex]=arr[thirdIndex],arr[secondIndex]
			thirdIndex-=1
	return arr

print(dnf([6,6,5,7,6,7,5,5]))
	 	    

		    
