import collections


def missingElement(arr1,arr2):

	d=collections.defaultdict(int)
	
	for element in arr2:
			d[element]+=1
	print d		
	for element in arr1:
		if(d[element] == 0):
			return element
		else:
			d[element]-=1


print missingElement([5,5,7,7],[5,7,7])

print missingElement([1,2,3,4,5,6,7],[3,7,2,1,4,6])

print missingElement([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])


