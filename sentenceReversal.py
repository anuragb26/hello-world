
def reverseSentence(s):
	l=len(s)
	i=0
	s ="".join(reversed(s))
	wordStart=0
	wordEnd=0
	while i < len:
		if(s[i]== ''):
			reverseWord()
			wordStart=i+1
			worEnd=i+1
		else:
			worEnd++


	return s

print reverseSentence("anurag bajaj")



