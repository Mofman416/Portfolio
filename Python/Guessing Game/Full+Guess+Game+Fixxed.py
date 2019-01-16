<<<<<<< HEAD
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
            time.sleep(2)
            exit()
        else:
            print("That is not a option try again")
            print()
            print()
            time.sleep(1)
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
    time.sleep(2)

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
            if low.isdigit() is True:
                high = input("Please set the highest number: ")
                print()
                if high.isdigit() is True and high > low:
                    game()
                    break
                if high.isdigit() is False:
                    print("Please input a valid number or choose a number higher than the lower number.")
                    print()
            if low.isdigit() is False:
                print("Please input a valid number.")
                print()
        elif choice.lower().startswith("g"):
            guess = input("Please set the number of guesses. ")
            print()
            if guess.isdigit() is True:########Error type to many numbers and you get a. I cant get it to do it again but try again later
                game()
                break
            if guess.isdigit() is False:
                print("Please input a valid integer.")
                print()
                print()
    return

#Main Game

def game():
    global low
    global high
    global guess
    global random_num
    low = int(low)
    high=int(high)
    random_num = random.randrange(low,high)
    guess = int(guess)
    guess_num = 0
    while guess_num != guess:
        guess_1=input("Guess a number between and.")####cant get the variable low and high to run in the string and if tried converting it to a string
        if guess_1.isdigit() is True:
            if int(guess_1)==random_num:
                print("You're Correct")
                print("You Win the number was",str(random_num),".")
                print()
                print()
                time.sleep(3)
                return menu()
            elif int(guess_1)<random_num:
                print("The number that you guessed is higher then then random number")
                guess_num+=1
                print(guess_num,"out of",guess, "you have done")
            elif int(guess_1)>random_num:
                print("The number that you guessed is lower then then random number")
                guess_num+=1
                print(guess_num,"out of 5 you have done")
        if guess_1.isdigit() is False:
            print("This is not a valid number please try again")
            
    print("You Lose the number was",str(random_num),".")
    print()
    print()
    time.sleep(2)
    return menu()

menu()
            


        
=======
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
            time.sleep(2)
            exit()
        else:
            print("That is not a option try again")
            print()
            print()
            time.sleep(1)
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
    time.sleep(2)

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
            if low.isdigit() is True:
                high = input("Please set the highest number: ")
                print()
                if high.isdigit() is True and high > low:
                    game()
                    break
                if high.isdigit() is False:
                    print("Please input a valid number or choose a number higher than the lower number.")
                    print()
            if low.isdigit() is False:
                print("Please input a valid number.")
                print()
        elif choice.lower().startswith("g"):
            guess = input("Please set the number of guesses. ")
            print()
            if guess.isdigit() is True:########Error type to many numbers and you get a. I cant get it to do it again but try again later
                game()
                break
            if guess.isdigit() is False:
                print("Please input a valid integer.")
                print()
                print()
    return

#Main Game

def game():
    global low
    global high
    global guess
    global random_num
    low = int(low)
    high=int(high)
    random_num = random.randrange(low,high)
    guess = int(guess)
    guess_num = 0
    while guess_num != guess:
        guess_1=input("Guess a number between and.")####cant get the variable low and high to run in the string and if tried converting it to a string
        if guess_1.isdigit() is True:
            if int(guess_1)==random_num:
                print("You're Correct")
                print("You Win the number was",str(random_num),".")
                print()
                print()
                time.sleep(3)
                return menu()
            elif int(guess_1)<random_num:
                print("The number that you guessed is higher then then random number")
                guess_num+=1
                print(guess_num,"out of",guess, "you have done")
            elif int(guess_1)>random_num:
                print("The number that you guessed is lower then then random number")
                guess_num+=1
                print(guess_num,"out of 5 you have done")
        if guess_1.isdigit() is False:
            print("This is not a valid number please try again")
            
    print("You Lose the number was",str(random_num),".")
    print()
    print()
    time.sleep(2)
    return menu()

menu()
            


        
>>>>>>> cf8c02e5d2e67bed4c877d82bc9da6ee212a0d2f
