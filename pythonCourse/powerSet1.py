def powerSet(items):
	N=len(items)
	for i in range(2**N):
		result=[]
		for j in range(N):
			if((i>>j)%2==1):
				result.append(items[j])
		yield result

def powerSetOne(items):
	result=[]
	result.append('')
	for elem in items:
		resultCopy=result[:]
		for item in result:
			resultCopy.append(elem+ str(item))
		result=resultCopy
		resultCopy=[]
	return result

#l=['a','b','c']

#print(powerSetOne(l))



def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N=len(items)
    for i in range(3**N):
        result1=[]
        result2=[]
        for j in range(N):
            if((i//3**j)%3==1):
                result1.append(items[j])
            elif((i//3**j)%3==2):
            	result2.append(items[j])
        yield (result1,result2)

#for item in powerSet(['a','b','c']):
#	print(item)

y=yieldAllCombos(['a','b'])
#print(next(y))
#for item in yieldAllCombos(['a','b']):
#	print(item)