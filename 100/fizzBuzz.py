'''fizzBuzz 
multiples of 3 print Fizz
multiples of 5 print Buzz
multiples of 3 and 5 print fizzBuzz
'''

def fizzBuzz():
	for i in range(100):
		if(i%3 ==0 and i%5==0):
			print ( str(i) + "fizzBuzz")
		elif(i%3==0):
			print ( str(i) + "fizz")
		elif(i%5==0):
			print ( str(i) + "Buzz")	


fizzBuzz()
