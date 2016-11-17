def makeEqualLength(l1,l2):
	if(l1 > l2):
		#l2 = "0"*(l1-l2) + l2
		return 1
	elif(l2 > l1):
		#l1= "0"*(l2-l1) + l1
		return 0

def addTwoBinary(s1,s2):
	l1=len(s1)
	l2=len(s2)
	maxLen=max(l1,l2)
	if(l1 > l2):
		s2="0"*(l1-l2) + str(s2)
	else:
		s1="0"*(l2-l1) + str(s1)
	res=[]
	carryBit=0
	res=[]
	for i in range(maxLen-1,-1,-1):
		bit1=int(s1[i])
		bit2=int(s2[i])
		sumBit=str(bit1 ^ bit2 ^ carryBit)
		carryBit=(bit1 and bit2) or (bit2 and carryBit) or (carryBit and bit1)
		res.insert(0,sumBit)
	if(carryBit==1):
		res.insert(0,str(carryBit))
	return "".join(res)

print(addTwoBinary("1100011","10"))

	
