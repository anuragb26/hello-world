 #wordFile="words.txt"

# f=open(wordFile)
# wordList=f.read().split()

# for word in wordList:
#	print (word)

word = "anurag"

print(word[:-3])
for i in range(len(word)):
	print (word[:i] + "_" + word[i+1:])