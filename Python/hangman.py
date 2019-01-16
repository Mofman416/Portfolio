# Hangman
# Michael Freeman
# 11/26

#imports
import random
import time

#constants
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

#Game Over
def game_over(wrong, HANGMAN):
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")

#This function shows up if you guess a letter already used.
def use(guess):
    print("You've already guessed the letter", guess)
    guess = input("Enter your guess: ")
    guess = guess.upper()

#This function is called when the player guessed the word.
def win(word):
    print("\nYou guessed it!")
    print("\nThe word was", word)

    input("\n\nPress the enter key to exit.")
    

print("Welcome to Hangman. Have fun!")

while wrong <MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
    
    while guess in used:
        use(guess)

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
    game_over(wrong, HANGMAN)

else:
    win(word)

