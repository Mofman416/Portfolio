# Hangman
# Michael Freeman
# 11/26

#imports
import random
import time

#constants
def hangman():
    HANGMAN = (
    """

    ---------
    |       |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    __________
    """,
    """
    ---------
    |       |
    |       O
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    __________
    """,
    """
    ---------
    |       |
    |       O
    |       +
    |       
    |      
    |
    |
    |
    |
    |  
    |
    |
    __________
    """,
    """
    ---------
    |       |
    |       O
    |      -+
    |
    |
    |
    |
    |
    |
    |
    |
    |
    __________
    """,
    """
    ---------
    |       |
    |       O
    |      -+-
    |       
    |       
    |
    |
    |
    |
    |  
    |
    |
    __________
    """,
    """
    ---------
    |       |
    |       O
    |      -+-
    |       |
    |
    |
    |
    |
    |
    |
    |
    |
    __________
    """,
    """
    ---------
    |       |
    |       O
    |      -+-
    |       |
    |      / 
    |
    |
    |
    |
    |  
    |
    |
    __________
    """,
    """
    ---------
    |       |
    |       O
    |      -+-
    |       |
    |      / \
    |
    |
    |
    |
    |  DEAD
    |
    |
    __________
    """)

    MAX_WRONG=len(HANGMAN)-1
    WORDS= ("OVERUSED", "CALM", "GUAM", "TAFFETA", "PYTHON")
    word = random.choice(WORDS) #The word the player will need to guess.
    so_far = "_"*len(word)
    wrong = 0 #number of wrong guesses the player made
    used = [] #The incorrect letters used.

def game():
    print("Welcome to Hangman. Have fun!")

    while wrong <MAX_WRONG and so_far != word:
        hangman()
        print(HANGMAN[wrong])
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, the word is:\n", so_far)

        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()
        
        while guess in used:
            print("You've already guessed the letter", guess)
            guess = input("Enter your guess: ")
            guess = guess.upper()

        used.append(guess)

        if guess in word:
            print("\nYes!", guess, "is in the word.")

            # create a new so_far to include guess
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
        else:
            print("\nSorry,", guess, "isn't in the word.")
            wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou've been hanged!")

    else:
        print("\nYou guessed it!")
    print("\nThe word was", word)

    input("\n\nPress the enter key to exit.")

game()
