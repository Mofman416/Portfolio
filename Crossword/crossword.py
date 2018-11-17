# Michael Freeman & Parker Gowans
#November 16th 2018
#4/5 Period

import time

#This is the Puzzle string.
puzzle = "ofunctionypwnoynjrzwehaziigydxriepnrnjtzallatpipbcteotedrzwiopoagbyfqfrpboeasidysvrlrinputdnmflppmcn"

#This displays the puzzle in rows as a function.
def display_puzzle():
    print(puzzle[0:10])
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:])
    print()

total = 0
point = 20
earn = point
attempts = 0
pointred = 0

word1_length=len("input")
word2_length=len("function")
word3_length=len("print")
word4_length=len("integer")
word5_length=len("string")
word6_length=len("operators")
word7_length=len("boolean")
word8_length=len("if")
word9_length=len("while")
word10_length=len("float")

#This is the crossword game
def crossword():
    global point
    global earn
    global attempts
    global pointred
    global total
    x=0
    while x==0:
        if playerguess.lower() == ans1:
            point + total
        else:
            print("Try again.")
            attempts += 1
            if pointred >= 5:
                new = point/2
                pointred += 1

#This is how the game opens.
def menu():
    print("Welcome to the crossword game!")
    print()

    ans = input("Would you like to play? Y/N ")
    print()

    while True:
        if ans.upper() == "Y" or ans.lower() == "yes":
            print("You will be asked a trivia question which will proceed to a crossword puzzle if answered correctly.")
            print()
        
            print("You can earn at most 20 points. Everytime you answer correctly half the points will be taken from you until you guess incorrectly 5 times.")
            print()

            print("Go for the perfect 200 points!!")
            print()

            print("Ready? Here we go!")
            print()
            time.sleep(5)
            game()
        elif ans.upper() == "N" or ans.lower() == "no":
            print("You're missing out on the game of the year 2018")
            print()
            time.sleep(1)
            menu()
        elif ans.lower() == "quit":
            exit()
        else:
            print("Invalid input, go home.")
            
menu()
