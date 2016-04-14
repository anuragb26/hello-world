import collections
def uniqueCharMyself(s):
	hash =collections.defaultdict(int)
	for letter in s:
		hash[letter]+=1
	for k,v in hash.items():
		if(v > 1):
			return False
	return True

def uniqueCharFirst(s):
	return len(set(s))== len(s)	

def uniqueCharSecond(s):
	seen=set()
	for letter in s:
		if (letter in seen):
			return False
		else:
			seen.add(letter)
	return True

print(uniqueCharMyself("ABCDE"))
print(uniqueCharMyself("ABCAAADE"))
print(uniqueCharFirst("ABCDE"))
print(uniqueCharFirst("ABCAAADE"))
print(uniqueCharSecond("ABCDE"))
print(uniqueCharSecond("ABCAAADE"))