input=input().strip().split()
print (input)

balance=int(input[0])
interestRate=float(input[1])

'''
paymentAmount=float(input[2])
#compInterest=0
remBalance=balance
monthlyInt=0
for i in range(12):
	remBalance=remBalance - (paymentAmount*remBalance)
	monthlyInt=(interestRate/12)*remBalance
	remBalance=remBalance+monthlyInt
	#print ("Month {0} and remaining balance is {1:.2f}".format(i+1,remBalance))
	#compInterest+= monthlyInt

print "Remaining balance: {0:.2f}".format(remBalance)
'''
'''
monthlyPymt=0
remBalance=balance
while(int(remBalance) > 0):
    monthlyPymt+=10
    print ("Monthly Payment: {0}".format(monthlyPymt))  
    remBalance=balance
    for i in range(12):
        remBalance = remBalance - monthlyPymt
        monthlyInt=(interestRate/12)*remBalance
        remBalance=remBalance+monthlyInt
    print ("Remaining Balance: {0:.2f}".format(remBalance))  
    

print ("Lowest Payment: {0}".format(monthlyPymt))  

'''

lowerBound=balance/12
upperBound=(balance*pow((1+interestRate),12))/12
print ("Upper Bound: {0} and Lower Bound : {1}\n".format(upperBound,lowerBound))
monthlyPymt = float((lowerBound+upperBound)/2)
remBalance=-1000000

while(int(remBalance) != 0):    
    monthlyPymt = float((lowerBound+upperBound)/2)
    print ("Upper Bound: {0:.2f} and Lower Bound : {1:.2f}".format(upperBound,lowerBound))
    print ("Monthly Payment: {0:.2f}\n".format(monthlyPymt))
    remBalance=balance
    for i in range(12):
        remBalance = remBalance - monthlyPymt
        monthlyInt=float((interestRate/12)*remBalance)
        remBalance=remBalance+monthlyInt
    print ("Remaining Balance: {0:.2f}\n".format(remBalance))    
    if(int(remBalance) <= 0):
        upperBound=monthlyPymt
    else:
        lowerBound=monthlyPymt 
print ("Lowest Payment: {0:.2f}".format(monthlyPymt))  


        
    
    
