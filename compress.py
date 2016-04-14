#strings are mutable so make a new string

def compress(s):
	
	length=len(s)
	#below two are standard edge cases for array comparison problems
	if(length==0):
		return
	if(length ==1):
		return s + "1"
	compress=""
	i=1
	count=1
	while(i<length):
		if(s[i]==s[i-1]):				#comparing two element together in one loop very important concept
			count+=1
		else:
			compress = compress + s[i-1]+ str(count)
			count=1
		i+=1
	compress = compress + s[i-1] + str(count)
	return compress
print(compress('AAAAABBBBCCCC'))
