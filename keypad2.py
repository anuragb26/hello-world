def combinationCounts(input1):
    
    letterList=['A','B','C','D','E','F','G','H','I','J']
    totalCount=0
    n=input1
    if(n<=0):
        return 0
    for letter in letterList:
        x=findCombinationForAlphabet(letter,n) 
        totalCount+=x
    return totalCount
    
    
def findCombinationForAlphabet(letter,n):
    
    if(n==1):
        return 1
    else:
        if(letter=='A'):
            return findCombinationForAlphabet('A',n-1) + findCombinationForAlphabet('B',n-1) + findCombinationForAlphabet('D',n-1)
        elif(letter=='B'):
            return findCombinationForAlphabet('B',n-1) + findCombinationForAlphabet('A',n-1) + findCombinationForAlphabet('C',n-1) + findCombinationForAlphabet('E',n-1)
        elif(letter=='C'):
            return findCombinationForAlphabet('C',n-1) + findCombinationForAlphabet('B',n-1) + findCombinationForAlphabet('F',n-1)
        elif(letter=='D'):
            return findCombinationForAlphabet('D',n-1) + findCombinationForAlphabet('A',n-1) + findCombinationForAlphabet('E',n-1) + findCombinationForAlphabet('G',n-1)
        elif(letter == 'E'):
            return findCombinationForAlphabet('D',n-1) + findCombinationForAlphabet('B',n-1) + findCombinationForAlphabet('E',n-1) + findCombinationForAlphabet('F',n-1) + findCombinationForAlphabet('H',n-1)
        elif(letter == 'F'):
            return findCombinationForAlphabet('F',n-1) + findCombinationForAlphabet('E',n-1) + findCombinationForAlphabet('C',n-1) + findCombinationForAlphabet('I',n-1)
        elif(letter == 'G'):
            return findCombinationForAlphabet('G',n-1) + findCombinationForAlphabet('D',n-1) + findCombinationForAlphabet('H',n-1)
        elif(letter == 'H'):
            return findCombinationForAlphabet('H',n-1) + findCombinationForAlphabet('E',n-1) + findCombinationForAlphabet('G',n-1) + findCombinationForAlphabet('I',n-1) + findCombinationForAlphabet('J',n-1)
        elif(letter == 'I'):
            return findCombinationForAlphabet('I',n-1) + findCombinationForAlphabet('F',n-1) + findCombinationForAlphabet('H',n-1)
        elif(letter== 'J'):
            return findCombinationForAlphabet('J',n-1) + findCombinationForAlphabet('H',n-1)

print(combinationCounts(3))
            
        
    
    

