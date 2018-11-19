# Michael Freeman & Parker Gowans
#November 16th 2018
#4/5 Period

import time

#This is the Puzzle string.
puzzle = "ofunctionypwnoynjrzwehaziigydxriepnrnjtzallatpipbcteotedrzwi"+"opoagbyfqfrpboeasidysvrlrinputdnmflppmcn"

#This displays the puzzle in rows as a function.
def display_puzzle():
    print("Row 0:", puzzle[0:10])
    print("Row 1:", puzzle[10:20])
    print("Row 2:", puzzle[20:30])
    print("Row 3:", puzzle[30:40])
    print("Row 4:", puzzle[40:50])
    print("Row 5:", puzzle[50:60])
    print("Row 6:", puzzle[60:70])
    print("Row 7:", puzzle[70:80])
    print("Row 8:", puzzle[80:90])
    print("Row 9:", puzzle[90:])
    print()

# These are the variables that the function uses.
total = 0
point = 20
earn = point
attempts = 0
pointred = 0

#This is the word length keys.

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
        ans = input("Question 1: This is what is used to get user defined values in a variable. Contrast Output. ")
        print()
        if ans.lower() == "input":
            total += earn
            attempts += 1
            i=0
            foundword=""
            earn = point
            print("Good Job! Now enter the index positions of 'Input' in this puzzle: ")
            print()
            display_puzzle()
            print()
            word1 = input("Enter the index positions of 'input'. ")
            print(puzzle.find('input'))
            while i < word1_length:
                index=word1[i]
                index=int(index)
                foundword=foundword+puzzle[index]
                i+=1
            if foundword == "input":
                print()
                print("You've tried to find 'input'...")
                print()
                time.sleep(2)
                print("You were correct!")
                print()
                x=1
            else:
                print("You've tried to find the word 'input'...")
                print(foundword)
                print()
                time.sleep(2)
                print("That's incorrect! Try again.")
                print()
            
            
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            if pointred <= 5:
                earn = point/2
                pointred += 1

#This is how the game opens.
def menu():
    print("Welcome to the crossword game!")
    print()

    ans = input("Would you like to play? Y/N You may also type 'Quit' if you want to quit. ")
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
            crossword()
        elif ans.upper() == "N" or ans.lower() == "no":
            print("You're missing out on the game of the year 2018")
            print()
            time.sleep(1)
            menu()
        elif ans.lower() == "quit":
            exit()
        else:
            print("Invalid input, go home.")
            break
            
menu()
