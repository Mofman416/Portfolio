import random
import time

global low
global high
global guess

low = 1
high = 100
guess = 5




print("Welcome to the Guessing Game!")
print()

print("Here are your options:")
print()

print("Play: You have five guesses to correctly guess a random number picked from a range of 1 to 100.")
print()

print("Advanced: Pick the number range or how many guesses you can start with.")
print()

print("Credits: Shows who made the game.")
print()

print("Quit: Closes the program.")
print()

choice = input("Please choose an option. ")
print()

while True:
    if choice.lower().startswith("p"):
        game()
        print()
        choice = input("What would you like to do now? Play, Advanced, Credits or Quit? ")
    elif choice.lower().startswith("a"):
        advanced()
        print()
        choice = input("What would you like to do now? Play, Advanced, Credits or Quit? ")
    elif choice.lower().startswith("c"):
        print("The Guessing Game.")
        print()

        print("Created by \nKyle Baldwin \nMichael Freeman")
        print()

        print("Game design by \nKyle Baldwin")
        print()

        print("Advanced Options by \n Michael Freeman")
        print()

        print("Created in Python")
        print()

        choice = input("What would you like to do now? Play, Advanced, Credits or Quit? ")
        print()
    elif choice.lower().startswith("q"):
        print("Thank you for playing!")
        time.sleep(3)
        exit()
