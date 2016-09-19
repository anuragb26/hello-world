input=raw_input().strip().split()
print (input)

balance=int(input[0])
interestRate=float(input[1])
paymentAmount=float(input[2])

#compInterest=0
monthlyInt=0
remBalance=balance
for i in range(12):
	remBalance=remBalance - (paymentAmount*remBalance)
	monthlyInt=(interestRate/12)*remBalance
	remBalance=remBalance+monthlyInt
	#print ("Month {0} and remaining balance is {1:.2f}".format(i+1,remBalance))
	#compInterest+= monthlyInt

print "Remaining balance: {0:.2f}".format(remBalance)
