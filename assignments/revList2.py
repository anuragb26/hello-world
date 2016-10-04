def deep_reverse(L):
	l=len(L)
	i=0
	while(i<(l/2)):
		print("{0} and {1}".format(i,l-i-1))
		L[i],L[l-1-i]=L[l-1-i],L[i]
		if(isinstance(L[i],list)):
			print("dr first {0}".format(L[i]))
			deep_reverse(L[i])
		if(isinstance(L[l-1-i],list)):
			print("dr second {0}".format(L[l-i-1]))
			deep_reverse(L[l-1-i])
		print("end of  while iteration")
		i+=1

def deep_reverseFunc(L):
    l=len(L)
    i=0
    while(i<l):
        if(isinstance(L[i],list)):
            L[i].reverse()
        i+=1
    L.reverse()



L=[[1,2],[2,3,4],[5,6,7]]
deep_reverseFunc(L)
print(L)