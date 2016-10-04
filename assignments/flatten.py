def flatten(aList):
	cList=[]
	for ele in aList:
		if isinstance(ele,list):
			cList.extend(flatten(ele))
		else:
			cList.append(ele)
	return cList





l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(l))