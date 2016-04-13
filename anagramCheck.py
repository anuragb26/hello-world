def anagramTest(s1,s2):

	s1 = s1.replace(" ","").lower()
	s2=s2.replace(" ","").lower()

	if(len(s1)!=len(s2)):
		return false

	count = {}

	for letter in s1:
		if(letter in count):
			count[letter]+=1
		else:
			count[letter]=1

	for letter in s2:
		if(letter in count):
			count[letter]-=1
		else:
			count[letter]=1

	for key in count:
		if(count[key]!=0):
			return False

	return True
print "Anagram Test \n"
print anagramTest('dog','god')
print "\n"
print anagramTest('clint eastwood','old west action')

