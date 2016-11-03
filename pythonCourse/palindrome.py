import unittest

def digits(x):
	''' Convert an integer into a list of digits.
	Args:
		x:The number whose digits we want
	Returns:
		A list of the digits,in order of x
	>>> digits(1234)
	[1,2,3,4]
	'''

	digs=[]
	while(x!=0):
		div,mod=divmod(x,10)
		digs.append(mod)
		x=mod
	return digs


def is_palindrome(x):
	digs=digits(x)

	for f,r in zip(digs,reversed(digs)):
		if f!=r:
			return False
		return True

class Tests(unittest.TestCase):

	def test_negative(self):
		self.assertFalse(is_palindrome(1234))

	def test_positive(self):
		self.assertTrue(is_palindrome(1234321))

	def test_single_digit(self):
		for i in range(10):
			self.assertTrue(is_palindrome(i))

if __name__='__main__':
	unittest.main()


