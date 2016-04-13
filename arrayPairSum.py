def arrayPairSum(arr,sum):
	if(len(arr) < 2):
		return
	seen = set()
	output = set()

	for k in arr:
		target = sum -k
		if(target not in seen):
			seen.add(k)
		else:
			print str(min(k,target)) + "+" + str(max(k,target)) + "=" + str(sum)


arrayPairSum([1,3,2,2],4)