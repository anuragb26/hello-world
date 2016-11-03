def nextLargestNumber(n):
	l=len(n)-1
	while( l >0 and n[l-1] > n[l]):
		l-=1
	if(l==0):
		return False
	x=n[l-1]
	smallest=l
	i=l+1
	while(i <=len(n)-1):
		if(n[i] > x and n[i] < n[smallest]):
			smallest=i
		i+=1
	n[l-1],n[smallest]=n[smallest],n[l-1]
	
	return "".join(n[:l] + sorted(n[l:]))

print(nextLargestNumber(list("534951")))
