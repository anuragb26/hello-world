# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words3.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("{0} words loaded".format(len(wordlist)))
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessed = True
    for c in secretWord:
        if c not in lettersGuessed:
            guessed=False 
            break

    return guessed



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedList=[]
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedList.append(letter)
        else:
            guessedList.append("_ ")
    return "".join(guessedList).strip()

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avalaibleLetters=list(string.ascii_lowercase)
    #copyAvailaible=avalaibleLetters[:]
    for c in lettersGuessed:
        if c in avalaibleLetters:
            avalaibleLetters.remove(c)

    return "".join(avalaibleLetters).strip()


    # FILL IN YOUR CODE HERE...
    
def startingMessage(wordLength):
    print("Welcome to the game, Hangman!\nI am thinking of a word that is {0} letters long.".format(wordLength))

def seperator():
    print("------------")

def showGuessPrompt(mistakesAllowed,avalaibleLetters):
    print("You have {0} guesses left.\nAvailable letters: {1}".format(mistakesAllowed,avalaibleLetters))
    c=input('Please guess a letter: ')
    return c

def showAlreadyPresentPrompt(currentStr):
    print("Oops! You've already guessed that letter: {0}".format(currentStr))
    seperator()

def showCorrectGuessMsg(updatedStr):
    print("Good Guess: {0}".format(updatedStr))
    seperator()

def showIncorrectGuessMsg(updatedStr):
    print("Oops! That letter is not in my word: {0}".format(updatedStr))
    seperator()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    wordToGuess=secretWord.lower()
    wordLength=len(wordToGuess)
    lettersGuessed=list()
    mistakesAllowed=8
    avalaibleLetters=string.ascii_lowercase
    startingMessage(wordLength)
    seperator()
    isGuessed=False
    currentStr="".join(["_ " for x in range(wordLength)]).strip()
    while(not isGuessed):
        c=showGuessPrompt(mistakesAllowed,avalaibleLetters)
        if c in lettersGuessed:
            showAlreadyPresentPrompt(updatedStr)
        else:
            lettersGuessed.append(c)
            updatedStr=getGuessedWord(wordToGuess,lettersGuessed)
            currCount=currentStr.count('_')
            updatedCount=updatedStr.count('_')
            if(currCount!=updatedCount):
                showCorrectGuessMsg(updatedStr)
            else:
                #print("coming in else")
                mistakesAllowed-=1
                showIncorrectGuessMsg(updatedStr)
                if(mistakesAllowed==0):
                    break
            avalaibleLetters=getAvailableLetters(lettersGuessed)
            if(isWordGuessed(wordToGuess,lettersGuessed)):
                isGuessed=True
    if(mistakesAllowed==0 and not isGuessed):
        print("Sorry, you ran out of guesses. The word was {0}".format(wordToGuess))
    elif(isGuessed):
        print("Congratulations, you won!")
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
secretWord='y'
print(secretWord)
hangman(secretWord)
