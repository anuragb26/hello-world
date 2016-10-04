def closest_power(base,num):
   lowerPower=0
   numC=num
   while(numC > base):
       numC=numC/base
       lowerPower+=1
   upperPower=lowerPower+1
   diffLower=abs(num-pow(base,lowerPower))
   diffUpper=abs(num-pow(base,upperPower))
   if(diffLower <= diffUpper):
       return lowerPower
   else:
       return upperPower

x=closest_power(4,12)
print(x)
