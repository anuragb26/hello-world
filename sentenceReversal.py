def reverseWord(word,start,end):
    reverseWord=""
    while(end>=start):
        reverseWord=reverseWord + word[end]
        end-=1
 #   print("in reverse word ",reverseWord)    
    return reverseWord
    

    
#Manual Reverse Sentence --> not to be used
def reverseSentence(sent):
    wordStart=-1
    wordEnd=-1
    reversedSentence=""
    length =len(sent)-1
    index=0
    while(index <=length):
       # print ("index is ",index, " and character is ",sent[index]," and wordstart and wordEnd ",wordStart," -> ",wordEnd)
        if(sent[index]==" " and wordEnd==-1 and wordStart==-1):
        #    print ("coming in first condition ",sent[index])
            reversedSentence=reversedSentence+sent[index]
        elif((sent[index]==" " or index==length) and wordEnd == -1):
           # print ("coming in second condition ",sent[index]," wordStart ",wordStart," wordEnd ",wordEnd)
            if(index == length):
                wordEnd=index
            else:
                wordEnd=index-1
            reversedSentence = reversedSentence + str(reverseWord(sent,wordStart,wordEnd)) + " "
            wordEnd=-1
            wordStart=-1
        elif(sent[index]!= " " and wordStart ==-1):
           #  print ("coming in third condition ",sent[index])
             wordStart=index
        index+=1
       
    return reverseWord(reversedSentence,0,length)


def reverseSentenceSecond(s):
	reverseSentence=" ".join(reversed(s.split()))
	return reverseSentence

def reverseSentenceThird(s):
	reverseSentence=" ".join(s.split()[::-1])
	return reverseSentence

def reverseSentenceFourth(s):
	reverseSentence=''
	temp=''
	for i in s:
		if(i!= ' '):
			temp=temp +i
		else:
			reverseSentence=temp + " " + reverseSentence
			temp=''
	reverseSentence=temp + ' ' + reverseSentence
	return reverseSentence

def reverseSentenceFifth(s):
	wordList=[]
	wordStart=''
	i=0
	length=len(s)
	while(i < length):
		if(s[i] != ' '):
			wordStart=i
			while(i < length and s[i] != ' '):
				i+=1
			wordList.append(s[wordStart:i])
		i+=1	

	return " ".join(reversed(wordList))




 
print(reverseSentence("abc def   ghi"))
print(reverseSentenceSecond("abc def   ghi"))
print(reverseSentenceThird("abc def   ghi"))
print(reverseSentenceFourth("  abc def   ghi  "))
print(reverseSentenceFifth("  abc def   ghi  "))    






