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
 
print("Something works")
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("bs " + str(binarySearch(testlist, 3)))
print("bs " + str(binarySearch(testlist, 13)))