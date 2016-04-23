def binarySearch(testlist,item):

	found=False
	start=0
	end=len(testlist)-1
	while(start <=end and not found):
		mid=(start+end)//2
		if(testlist[mid]==item):
			found=True
		elif(item>testlist[mid]):
			start=mid+1
		elif(item < testlist[mid]):
			end=mid-1
	return found


def recursiveBinarySearch(testList,start,end,item):
	if(start>end):
		return False
	else:	
		mid=(start+end)//2
		if(testlist[mid]==item):
			return True
		elif(item < testList[mid]):
			return recursiveBinarySearch(testList,start,mid-1,item)
		elif(item > testList[mid]):
			return recursiveBinarySearch(testList,mid+1,end,item)	
 
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("bs " + str(binarySearch(testlist, 3)))
print("bs " + str(binarySearch(testlist, 13)))

print("bs " + str(recursiveBinarySearch(testlist,0,len(testlist)-1,3)))
print("bs " + str(recursiveBinarySearch(testlist, 0,len(testlist)-1,32)))




