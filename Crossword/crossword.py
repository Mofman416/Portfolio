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
    
    #Question 1
    
    x=0
    while x==0:
        ans = input("Question 1: This is what is used to get user defined values in a variable. Contrast Output. ")
        print()
        if ans.lower() == "input":
            total += earn
            i=0
            foundword=""
            earn = point
            pointred = 0
            print("Good Job! Now enter the index positions of 'Input' in this puzzle: ")
            print()
            display_puzzle()
            f=0
            while f==0:
                print()
                word1 = input("Enter the index positions of 'input'. ")
                if word1.isdigit():
                    while i < word1_length*2:
                        z = i + 2
                        index=word1[i:z]
                        index=int(index)
                        foundword=foundword+puzzle[index]
                        i+=2
                    if foundword == "input":
                        print()
                        print("You've tried to find 'input'...")
                        print()
                        time.sleep(2)
                        print(foundword)
                        print()
                        print("You were correct!")
                        print()
                        x=1
                        f=1
                    elif foundword != "input":
                        print()
                        print("You've tried to find the word 'input'...")
                        print()
                        time.sleep(2)
                        print(foundword)
                        print()
                        print("That's incorrect! Try again.")
                        print()
                        attempts += 1
                        print("That's " + attempts + " attempts.")
                    else:
                        print()
                        print("Please input a valid response. No letters or decimals please.")
                        print()
                        break
                    
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's " + attempts + " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1

    #Question 2
                
    x=0
    while x==0:
        ans = input("Question 2: This is what is used to put code in a 'package' that is easily reusable. Rhymes with Junction. ")
        print()
        if ans.lower() == "function":
            total += earn
            i=0
            foundword=""
            earn = point
            pointred = 0
            print("Good Job! Now enter the index positions of 'function' in this puzzle: ")
            print()
            display_puzzle()
            f=0
            while f==0:
                print()
                word2 = input("Enter the index positions of 'function'. ")
                if word2.isdigit():
                    while i < word2_length*2:
                        z = i + 2
                        index=word1[i:z]
                        index=int(index)
                        foundword=foundword+puzzle[index]
                        i+=2
                    if foundword == "function":
                        print()
                        print("You've tried to find 'input'...")
                        print()
                        time.sleep(2)
                        print(foundword)
                        print()
                        print("You were correct!")
                        print()
                        x=1
                        f=1
                    elif foundword != "function":
                        print()
                        print("You've tried to find the word 'input'...")
                        print()
                        time.sleep(2)
                        print(foundword)
                        print()
                        print("That's incorrect! Try again.")
                        print()
                        attempts += 1
                        print("That's " + attempts + " attempts.")
                    else:
                        print()
                        print("Please input a valid response. No letters or decimals please.")
                        print()
                        break
                    
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's " + attempts + " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1

    #Question 3

    x=0
    while x==0:
        ans = input("Question 3: This is used to show output. ")
        print()
        if ans.lower() == "print":
            total += earn
            i=0
            foundword=""
            earn = point
            pointred = 0
            print("Good Job! Now enter the index positions of 'print' in this puzzle: ")
            print()
            display_puzzle()
            f=0
            while f==0:
                print()
                word3 = input("Enter the index positions of 'print'. ")
                if word3.isdigit():
                    while i < word3_length*2:
                        z = i + 2
                        index=word1[i:z]
                        index=int(index)
                        foundword=foundword+puzzle[index]
                        i+=2
                    if foundword == "print":
                        print()
                        print("You've tried to find 'print'...")
                        print()
                        time.sleep(2)
                        print(foundword)
                        print()
                        print("You were correct!")
                        print()
                        x=1
                        f=1
                    elif foundword != "print":
                        print()
                        print("You've tried to find the word 'print'...")
                        print()
                        time.sleep(2)
                        print(foundword)
                        print()
                        print("That's incorrect! Try again.")
                        print()
                        attempts += 1
                        print("That's " + attempts + " attempts.")
                    else:
                        print()
                        print("Please input a valid response. No letters or decimals please.")
                        print()
                        break
                    
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's " + attempts + " attempts.")
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

            print("The crossword puzzle takes two digit numbers. If you want to put in a letter from the top row be sure to include the 0 (i.e. a letter on the top row three spaces to the right would be 02).")
            print()

            print("Ready? Here we go!")
            print()
            time.sleep(5)
            crossword()
            break
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
