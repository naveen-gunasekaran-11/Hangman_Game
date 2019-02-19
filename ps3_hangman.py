# Hangman game
#

import random
import string

WORDLIST_FILENAME = "words.txt"

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


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
    flag = True;
    for i in secretWord:
        if i not in lettersGuessed:
            flag = False;
            break;
    return flag;


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    test_string = "";
    guessed_string = "";
    for i in range (len(secretWord)):
        test_string = test_string + "_" + " ";
    index = 0;
    guessed_string = test_string;
    for j in lettersGuessed: 
        if j in secretWord:
            for k in range (len(secretWord)):
                if secretWord[k] == j:
                    index = k; 
                    for z in range (0, len(test_string), 2):
                        if z == index+index: 
                            guessed_string = test_string[:z] + j + test_string[z+1:];
                            test_string = guessed_string;
                            break;

    return guessed_string;

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lowercase_string = ""
    available_guess_string = "";
    lowercase_string = string.ascii_lowercase
    for i in lowercase_string:
        if (i not in lettersGuessed):
            available_guess_string = available_guess_string + i;
    return available_guess_string;
   

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
    num_guesses = 8;
    lettersGuessed = [];
    was_word_guessed = False;
    
    print ("Welcome to the game, Hangman!");
    length_secret_word = len (secretWord);
    print ("I am thinking of a word that is " + str(length_secret_word) + " letters long.");

    while num_guesses != 0:
        print ("-------------");
        print ("You have " + str(num_guesses) + " guesses left.");
        print ("Available letters: " + getAvailableLetters(lettersGuessed));
        user_input = str(input("Please guess a letter: "));
        if (user_input in lettersGuessed):
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed));
        else:
            lettersGuessed.append(user_input);
            if (user_input in secretWord):
                print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed));
            else:
                print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed));
                num_guesses = num_guesses - 1;
            
            if (isWordGuessed(secretWord, lettersGuessed)):
                was_word_guessed = True;
                break;
    print ("-------------");
    if (was_word_guessed):
        print ("Congratulations, you won!");
    else:
        print ("Sorry, you ran out of guesses. The word was " + secretWord + ".");


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
