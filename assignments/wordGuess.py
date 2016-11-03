import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    s=list(string.ascii_lowercase)
    sCopy=s[:]
    print(s)
    for c in sCopy:
        if c in lettersGuessed:
            print(" c {0}".format(c))
            s.remove(c)
    return "".join(s)  


print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))