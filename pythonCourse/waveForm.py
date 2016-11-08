arr=[10, 5, 6, 3, 2, 20, 100, 80]
arr=[20, 10, 8, 6, 4, 2]
arr=[2, 4, 6, 8, 10, 20]
arr=[3, 6, 5, 10, 7, 20]
def waveForm(arr):
	l=len(arr)
	for i in range(0,l,2):
		'''
		if(i==0 and i+1 < l):
			if(arr[i] < arr[i+1]):
				arr[i],arr[i+1]=arr[i+1],arr[i]
		elif(i==l-1):
			if(arr[i] < arr[i-1]):
				arr[i],arr[i-1]=arr[i-1],arr[i]
		else:
			if(arr[i] < arr[i-1]):
				arr[i],arr[i-1]=arr[i-1],arr[i]
			if(arr[i] < arr[i+1]):
				arr[i],arr[i+1]=arr[i+1],arr[i]
		'''				
		if(i>0 and arr[i] < arr[i-1]):
			arr[i],arr[i-1]=arr[i-1],arr[i]
		if(i<l-1 and arr[i] < arr[i+1]):
			arr[i],arr[i+1]=arr[i+1],arr[i]

print("previously {0}".format(arr))
waveForm(arr)
print("after {0}".format(arr))
