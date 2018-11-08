#Michael Freeman and Kyle Baldwin
#November 6th, 2018

import random
import time


low = 1
high = 100
guess = 5

#Menu

def menu():
    
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
        if choice.lower().startswith("play"):
            return game()
        elif choice.lower().startswith("advanced"):
            return advanced()
        elif choice.lower().startswith("credit"):
            return credit()
        elif choice.lower().startswith("quit"):
            print("Thank you for playing!")
            time.sleep(3)
            exit()
        else:
            print("That is not a option try again")
            print()
            time.sleep(3)
            return menu()


#Credits
        
def credit():
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
    print()
    time.sleep(3)

    return menu()



#Advanced game 

def advanced():
    global high
    global low
    global guess
    while True:
        choice = input("Would you like to change the number range (N) or the amount of guesses (G)? ")
        print()
        if choice.lower().startswith("n"):
            low = input("Please set the lowest number: ")
            print()
            if low.isdigit():
                high = input("Please set the highest number: ")
                print()
                if high.isdigit() and high > low:
                    game()
                    break
                else:
                    print("Please input a valid number or choose a number higher than the lower number.")
                    print()
            else:
                print("Please input a valid number.")
                print()
        elif choice.lower().startswith("g"):
            guess = input("Please set the number of guesses. ")
            print()
            if guess.isdigit():
                game()
                break
            else:
                print("Please input a valid integer.")
                print()
                print()
    return

#Main Game

def game():
    global low
    global high
    global guess
    low = int(low)
    high=int(high)
    guess = int(guess)
    random_num = random.randrange(low,high)
    guess_num = 0
    while guess_num <= guess:
        guess_1=input("Guess a number between 1 and 100 ")
        if guess_1.isdigit():
            if int(guess_1)==random_num:
                print("You're Correct")
                print("You Win")
                print()
                print()
                return menu()
            
            elif int(guess_1)>random_num:
                print("The number that you guessed is higher then then random number")
                guess+=1
            elif int(guess_1)<random_num:
                print("The number that you guessed is lower then then random number")
                guess_num+=1
                if guess_num== guess:
                    print("You Lose")
                    print()
                    print()
                    time.sleep(5)
                    return menu()
        else:
            print("This is not a valid number please try again")

menu()
            


        
