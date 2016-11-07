import unittest
import os


def analyzeText(fileName):
	
	lines=0
	chars=0
	with open(fileName,'r') as f:
		for line in f:
			lines+=1
			chars+=len(line)

	return lines,chars

class TestCase(unittest.TestCase):


	def setUp(self):
		self.fileName="abc.txt"
		with open(self.fileName,'w') as f:
			f.write('abcdefgni\n'
				'qwerty\n'
				'can long endure\n'
				)

	def tearDown(self):
		try:
			os.remove(self.fileName)
		except:
			pass

	def test_function_runs(self):
		analyzeText(self.fileName)

	def test_line_count(self):
		self.assertEqual(analyzeText(self.fileName)[0],3)

	def test_character_count(self):
		self.assertEqual(analyzeText(self.fileName)[1],33)

	def test_no_such_file_exists(self):
		with self.assertRaises(IOError):
			analyzeText('aba')

	def test_file_deleted(self):
		self.assertTrue(os.path.exists(self.fileName))

if __name__ == '__main__':
	unittest.main()