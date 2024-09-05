# Coding Challenge 3, hangman.py
# Name:Shubham Dahal
# Student No:2228047

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
alphabets = string.ascii_lowercase
# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):
    """
    Chooses a random word from those available in the wordlist

    Args:
        all_words (list): list of available words (strings)

    Returns:
        a word from the wordlist at random
    """
    return random.choice(all_words)


# end of helper code


def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    
    print("Loading word list from file: words.txt")
    # open function opens file and return it as file
    a = open(WORDLIST_FILENAME, 'r')
    b = a.readline()
    all_words = b.split()
    print(' ', len(all_words), 'words brought')
    return all_words
#return function exits and tells Python to continue executing the main program

wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far

    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    
    guessed = []
#Loop to tell whether word is guessed or not
    for letters in word:
        if letters in letters_guessed:
            guessed.append(True)
        else:
            guessed.append(False)
    if False in guessed:
        return False
    else:
        return True

#to get the guessed word
def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far

    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """

    alpha = ''
    for char in word:
        alpha += (char if char in letters_guessed else '_ ')
    return alpha


def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed

    Args:
        letters_guessed: list (of strings), which letters have been guessed

    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """

    global alphabets
    for char in alphabets:
        if char not in letters_guessed:
            alphabets = alphabets.replace(letters_guessed, "")
            print(alphabets)
            return alphabets


def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    print("---------------")

    letters_guessed = ""
    correct_guess = []
    tries = 10
    guessed = False
    global alphabets
    stop = 0
#while loop to check guessed and the no of tries    
    while not guessed and tries > 0:
        if stop == 1:
            guessed = True
            break
        guess = input("Can you Guess a random letter:").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print("This letter is already guessed")
                print(letters_guessed, "\n")
                print(tries, "tries remained")
                print(get_guessed_word(guess, letters_guessed))
            elif guess not in word:
                print(guess, "please witer in word: {0}".format(
                    get_guessed_word(word, letters_guessed)))
                tries -= 1
                letters_guessed = letters_guessed+""+guess
                get_remaining_letters(guess)
                print(letters_guessed, "\n")
                print(tries, "tries remained")
            else:
                print("Congrats ", guess, " is in the word")
                letters_guessed = letters_guessed+""+guess
                get_remaining_letters(guess)
                correct_guess.append(guess)
                print(letters_guessed, "\n")
                print(tries, "tries remained")
                print('Good guess: {0}'.format(
                    get_guessed_word(word, letters_guessed)))
                if is_word_guessed(word, letters_guessed):
                    stop = 1
        else:
            print("Sorry !! Guess Again")
    if guessed:
        print("Congraulations, you have won")
        score = tries*len(word)
        alphabets = string.ascii_lowercase
        print("your score is", score)
    else:
        print("sorry, zero tries remains. The word was " +
              word+" better luck next time:")
        score = tries*len(word)
        alphabets = string.ascii_lowercase
        print("you have scored :", score)
#taking input from user
    def ask_user():
        choice = input("Do u wish play again Y/N").upper()
        if choice == "Y":
            word = choose_random_word(wordlist)
            hangman(word)
        elif choice == "N":
            print("we want to thank you for playing this hangman game")
        else:
            print("enter valid choice")
            return ask_user()
    ask_user()


# -----------------------------------
# Driver function for the program
if __name__ == "__main__":
    # Uncomment the line below once you have finished testing.
    word = choose_random_word(wordlist)
# Uncomment the line below once you have implemented the hangman function.
    hangman(word)
